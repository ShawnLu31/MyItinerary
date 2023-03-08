import googlemaps
import json
import random
import Itn_keyword as kw
from Itn_requirements import Requirements 

def get_active_requirement():
    pass

def get_current_location():
    location = (22.997409807642487, 120.22060180281467)
    return location

"""
This function search the places according to the command, and return a place.
@cmd:
    'restaurant', return a place with type 'restaurant'
    'tourist_attraction', return a place with a type 'tourist_attraction'
"""
def search(place_type):
    gmaps = googlemaps.Client(key=kw.API_KEY)
    
    result = gmaps.places_nearby(
        location=get_current_location(),
        radius=1000,
        type=place_type,
        language='zh-TW'
    )

    place_id = pick_place(result['results'], 2)

    with open('./test/detail.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        

    return place_id

"""
This function return a place id.
Choose only one place from candidates in 3 ways:
    1. random
    2. rating score
    3. distance
"""
def pick_place(candidates, way):
    if way == 1:
        index = random.randint(0, len(candidates))
        return candidates[index]['place_id']
    elif way == 2:
        rating_list = [place['rating'] for place in candidates]
        print(rating_list)
        index = rating_list.index(max(rating_list))
        print(index)
        return candidates[index]['place_id']
    elif way == 3:
        pass
    else:
        print('ERROR, No such pick way.')
        return None


def search_directions(place):
    pass

