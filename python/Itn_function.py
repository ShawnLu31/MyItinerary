import googlemaps
import json
import random
import numpy as np
import Itn_keyword as kw
import Itn_requirements as Rq 
import Itn_database as Db

gmaps = googlemaps.Client(key=kw.API_KEY)

def get_keyword_list(types):
    active_requirement = Rq.get_reqiurements(types)
    keyword_list = ""
    for rq in active_requirement:
        keyword_list += rq + " "

    return keyword_list

def get_location(loc):
    if isinstance(loc, tuple):
        return loc
    if isinstance(loc, str):
        result = gmaps.place(
            place_id=loc,
            fields=['geometry/location'],
            language='zh-TW',
        )
        lat = result['result']['geometry']['location']['lat']
        lng = result['result']['geometry']['location']['lng']
        return (lat, lng) 

"""
This function search the places according to the command, and return a place id.
@place_type:
    'restaurant', return a place with type 'restaurant'
    'tourist_attraction', return a place with a type 'tourist_attraction'
@location:
    'current', search location is current location.
    'attraction', search location is about requirement attraction.
    else , is default location
"""
def search_place(pl_type, loc, keyword_list, min_price, max_price):
    rad_l = [1000, 10000, 50000]
    for rad in rad_l:
        result = search_nearby(
            pl_type, 
            get_location(loc), 
            rad, 
            keyword_list, 
            min_price, 
            max_price
        )

        if result['status'] == 'OK':
            place_id = pick_place(get_location(loc), result['results'], 3)
            dump_json(pl_type, result)
            return place_id

    return None

def search_nearby(place_type, location, rad, keyword_list, min_price, max_price):
    result = gmaps.places_nearby(
        location=location,
        radius=rad,
        keyword=keyword_list,
        min_price=min_price,
        max_price=max_price,
        type=place_type,
        language='zh-TW',
    )

    return result

def get_active_requirement(sub_reqs):
    if sub_reqs == 'num_member':    
        return
    if sub_reqs == 'select_set':  
        return  
    if sub_reqs == 'attractions':   
        return 
    if sub_reqs == 'food':    
        keyword_list = get_keyword_list(['food'])
        return keyword_list
    
    if sub_reqs == 'price':   
        price = Rq.get_reqiurements(['price'])
        if len(price) == 0:
            min_price, max_price = 0, 3
        else:
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
        return min_price, max_price
    
    if sub_reqs == 'entertainment':  
        return  
    if sub_reqs == 'geo_distance':    
        return
    if sub_reqs == 'transport_distance':    
        return

def get_budget():
    return Rq.budget

def get_from_database(type):
    table = Db.getData(type)
    return table
"""
This function return a place id.
Choose only one place from candidates in 3 ways:
    1. random
    2. rating score
    3. distance
"""
def pick_place(origin, candidates, way):
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
        place_loc = np.array([(place['geometry']['location']['lat'], place['geometry']['location']['lng']) for place in candidates])
        dist = abs(place_loc - np.array(origin))
        sum_dist = np.sum(dist, axis=1)
        index = np.argmin(sum_dist)
        return candidates[index]['place_id']
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
    f.close
    
