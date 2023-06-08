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
def pick_place_of_database(database):
    while True:
        index = random.randint(0, len(database) -1)
        if database[index] != None:
            break
    return database[index]

def search_onekey():
    # 處理需求
        # 人數
        # 景點
        # 餐廳
    food_keyword = Fc.get_active_requirement('food')
    min_price, max_price = Fc.get_active_requirement('price')
        # 娛樂
        # 距離 
        # 預算
    budget = Fc.get_budget()

    # 小型 2 food, 2 attr, 1 night
    # 中型 4 food, 4 attr, 1-2 night
    attractions = list(Fc.get_from_database('attractions'))
    hotels = list(Fc.get_from_database('hotels'))
    hotel = None

    for index in range(3):
        while True:
            
            if int(budget) >= 2000:
                while True:
                    # get hotel
                    hotel = pick_place_of_database(hotels)
                    print(f'hotel {hotel[2]}, {type(hotel[2])}')
                    if hotel[2] < int(budget):
                        break

            # get attr from base
            attr1 = pick_place_of_database(attractions)
            attractions.remove(attr1)
            attr2 = pick_place_of_database(attractions)
            attractions.append(attr1)

            # get  food
            food1_id = Fc.search_place('restaurant', attr1[0], food_keyword, min_price, max_price)
            food2_id = Fc.search_place('restaurant', attr2[0], food_keyword, min_price, max_price)
            if food1_id != None and food2_id != None:
                print("Find food")
                break
        
        result = {
            'hotel': Fc.get_place_details(hotel[0]) if hotel is not None else None,
            'attr1': Fc.get_place_details(attr1[0]),
            'attr2': Fc.get_place_details(attr2[0]),
            'food1': Fc.get_place_details(food1_id),
            'food2': Fc.get_place_details(food2_id),
        }
        fname = f'result{index}'
        Fc.dump_json(fname , result)
            
    return 

def search_reqiurement(stamp):
    pass

def search_reqiurement_strict():
    pass




