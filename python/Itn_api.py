import Itn_function as Fc

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
def search_onkey():
    # get restaurant
    place_1_id = Fc.search_place('restaurant', 'default')
    place_1 = Fc.get_place_details(place_1_id)

    # get attractions
    place_2_id = Fc.search_place('tourist_attraction', 'default')
    place_2 = Fc.get_place_details(place_2_id)

    route = Fc.search_directions(place_1_id, place_2_id)

    result = {'restaurant':place_1, 'attraction':place_2, 'route':route}
    Fc.dump_json('result', result)

    return 

def search_onekey_storage():
    pass

def search_reqiurement():
    pass

def search_reqiurement_strict():
    pass

def search_reqiurement_storage():
    pass


