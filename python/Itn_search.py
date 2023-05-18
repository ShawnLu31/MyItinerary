import Itn_function as Fc
import random
"""
show itinerary
"""
def show_itinerary_detail():
    pass

def show_itinerary_on_map():
    pass

"""
itinerary detail
"""
def show_location_info():
    pass

def zoom_location_on_map():
    pass

def show_transport_info():
    pass

def zoom_transport_on_map():
    pass
    
"""
search algorithm API
"""
attr = [{'place_name':"臺南市美術館2館", 
         'place_id':"ChIJQW7Ewnx2bjQR2vkI8YSRFXM",
         'cost': 200 },
         {'place_name':"安平樹屋", 
          'place_id':"ChIJlynOByF3bjQR_IzNSlgH-Ss",
          'cost': 70},
          {'place_name':"赤崁樓", 
          'place_id':"ChIJbYl7d2F2bjQRnFdvyMBuZfI",
          'cost': 50},
         ]
def search_onekey(stamp):
    # get restaurant

    att = attr[random.randint(0, 2)]['place_id']

    place_1_id = Fc.search_place('restaurant', att, ['food', 'price'])
    if place_1_id != None:
        print("Find place_1")
        place_1 = Fc.get_place_details(place_1_id)

    # get attractions

    place_2_id = att
    if place_2_id != None:
        print("Find place_2")
        place_2 = Fc.get_place_details(place_2_id)

    if place_1_id != None and place_2_id != None:
        route = Fc.search_directions(place_1_id, place_2_id)

    if place_1_id != None and place_2_id != None:
        result = {'restaurant':place_1, 'attraction':place_2, 'route':route}
        fname = 'result' + stamp
        Fc.dump_json(fname , result)
    else:
        print("stamp \"{0}\" Not Found!".format(stamp))
    
    return 

def search_onekey_storage():
    pass

def search_reqiurement(stamp):
    # get restaurant

    place_1_id = Fc.search_place('restaurant', (22.997409807642487, 120.22060180281467), ['food', 'price'])
    if place_1_id != None:
        print("Find place_1")
        place_1 = Fc.get_place_details(place_1_id)

    # get attractions

    place_2_id = Fc.search_place('tourist_attraction', (22.997409807642487, 120.22060180281467), ['entertainment'])
    if place_2_id != None:
        print("Find place_2")
        place_2 = Fc.get_place_details(place_2_id)

    if place_1_id != None and place_2_id != None:
        route = Fc.search_directions(place_1_id, place_2_id)

    if place_1_id != None and place_2_id != None:
        result = {'restaurant':place_1, 'attraction':place_2, 'route':route}
        fname = 'result' + stamp
        Fc.dump_json(fname , result)
    else:
        print("stamp \"{0}\" Not Found!".format(stamp))

def search_reqiurement_strict():
    pass

def search_reqiurement_storage():
    pass


