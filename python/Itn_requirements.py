reqiurements_list = {
    'num_member' : {
        'one': False, 
        'two': False, 
        'three': False, 
        'four': False, 
        'five': False
        },
    'select_set' : {
        'attractions': False, 
        'food': False, 
        'entertainment': False
        },
    'attractions' : {
        '臺南市美術館2館': False, 
        '安平古堡': False,
        '赤崁樓': False,
        '藍晒圖文創園區': False,
        '南紡購物中心': False
        },
    'food' : {
        'taiwanese': False, 
        'japanese': False, 
        'italian': False, 
        'french': False, 
        'fast food': False, 
        'exotic': False, 
        'vegetarian': False
        },
    'price' : {
        'low': False, 
        'normal': False, 
        'medium': False, 
        'high': False
        },
    'entertainment' : {
        'movie': False, 
        'shopping': False,
        'romance': False, 
        'sports': False, 
        'party': False
        },
    'geo_distance' : {
        'close': False, 
        'middle': False, 
        'far': False
        },
    'transport_distance' : {
        'short': False, 
        'half': False, 
        'long': False, 
        'hourup': False
        }
}
place_type = [
        'restaurant',
        'movie_theater',
        'tourist_attraction',
        'shopping_mall'
]

budget = 1000

def modify_reqiurements(rq, value):
    for type in reqiurements_list.keys():
        if rq in  reqiurements_list[type].keys():
            reqiurements_list[type][rq] = value

"""
getReqiurement:
@types, a list with what kinds of requirement should be return:
    'all', 'num_member',   ...
"""
def get_reqiurements(types):
    actice_reqiurements = []
    if not types:
        print("Error, empty list!")

    else:
        if types == ['all']:
            types = ['num_member', 'select_set', 'attractions', 'food', 'price', 'entertainment', 'geo_distance', 'transport_distance',  'transport_distance']

        for type in types:
            for key, value in reqiurements_list[type].items():
                if value == True:
                    actice_reqiurements.append(key)

    return actice_reqiurements

def clear_requirements():
    for _, dic in reqiurements_list.items():
        for key in dic:
            dic[key] = False
