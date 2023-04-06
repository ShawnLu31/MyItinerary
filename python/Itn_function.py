import googlemaps
import json
import random
import Itn_keyword as kw
import Itn_requirements as Rq 

gmaps = googlemaps.Client(key=kw.API_KEY)

def get_keyword_list(types):
    active_requirement = Rq.get_reqiurements(types)
    keyword_list = ""
    for rq in active_requirement:
        keyword_list += rq + " "

    return keyword_list

def get_search_location(type):
    if type == 'current':
        pass
    elif type == 'attraction':
        pass
    else:
        default_location = (22.997409807642487, 120.22060180281467)
        return default_location
"""
This function search the places according to the command, and return a place id.
@place_type:
    'restaurant', return a place with type 'restaurant'
    'tourist_attraction', return a place with a type 'tourist_attraction'
@location_type:
    'current', search location is current location.
    'attraction', search location is about requirement attraction.
    else , is default location
"""
def search_place(place_type, location_type, requirements):

    pl_type, keyword_list, min_price, max_price = analye_requirements(requirements)

    rad_l = [1000, 10000, 50000]
    for rad in rad_l:
        result = search_nearby(
            place_type if pl_type is None else pl_type, 
            location_type, 
            rad, 
            keyword_list, 
            min_price, 
            max_price
        )

        if result['status'] == 'OK':
            place_id = pick_place(result['results'], 1)
            dump_json(place_type if pl_type == None else pl_type, result)
            return place_id

    return None

def search_nearby(place_type, location_type, rad, keyword_list, min_price, max_price):
    result = gmaps.places_nearby(
        location=get_search_location(location_type),
        radius=rad,
        keyword=keyword_list,
        min_price=min_price,
        max_price=max_price,
        type=place_type,
        language='zh-TW',
    )

    return result

def analye_requirements(requirements):
    keyword_list = ""
    place_type = None
    min_price = None
    max_price = None
    for rq in requirements:
        if rq == 'food':
            keyword_list = get_keyword_list(['food'])
            place_type = Rq.place_type[0]

        if rq == 'price':
            price = Rq.get_reqiurements(['price'])

            if price == []:
                continue
            
            if price[0] == 'low':
                min_price = 0
            elif price[0] == 'normal':
                min_price = 1
            elif price[0] == 'medium':
                min_price = 2
            elif price[0] == 'high':
                min_price = 3
            else:
                min_price = 0

            if price[-1] == 'low':
                max_price = 0
            elif price[-1] == 'normal':
                max_price = 1
            elif price[-1] == 'medium':
                max_price = 2
            elif price[-1] == 'high':
                max_price = 3
            else:
                max_price = 3

        if rq == 'entertainment':
            entertainment = Rq.get_reqiurements(['entertainment'])

            for ent in entertainment:
                if ent == 'movie':
                    place_type = Rq.place_type[1]
                if ent == 'shopping':
                    place_type = Rq.place_type[3]
                if ent == 'romance':
                    pass


    print(place_type, ",", keyword_list, min_price, max_price)
    return place_type, keyword_list, min_price, max_price
"""
This function return a place id.
Choose only one place from candidates in 3 ways:
    1. random
    2. rating score
    3. distance
"""
def pick_place(candidates, way):
    if len(candidates) == 0:
        return None

    if way == 1:
        index = random.randint(0, len(candidates) - 1)
        return candidates[index]['place_id']

    elif way == 2:
        rating_list = [place['rating'] for place in candidates]
        index = rating_list.index(max(rating_list))
        return candidates[index]['place_id']

    elif way == 3:
        pass

    else:
        print('ERROR, No such pick way.')
        return None

def get_place_details(id):
    details = gmaps.place(
        place_id=id,
        fields=['formatted_address', 'name', 'geometry/location', 'place_id', 'rating', 'url', 'type'],
        language='zh-TW',
    )

    return details

def search_directions(ori, dest):
    route = gmaps.directions(
        origin='place_id:' + ori,
        destination='place_id:' + dest,
    )

    return route
    
"""
For debug
"""
def dump_json(name, data):
    fname = './test/' + name + '.json'
    with open(fname, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
