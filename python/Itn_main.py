import responses
import googlemaps
from datetime import datetime
import json

import Itn_api as api
import Itn_requirements as Rq 

if __name__ == '__main__':
    # 範例 1
    Rq.modify_reqiurements('food', 'japanese', True)
    Rq.modify_reqiurements('price', 'normal', True)
    api.search_reqiurement('1')
    Rq.clear_requirements()

    # 範例 2
    Rq.modify_reqiurements('food', 'fast food', True)
    Rq.modify_reqiurements('entertainment', 'movie', True)
    Rq.modify_reqiurements('price', 'low', True)
    api.search_reqiurement('2')
    Rq.clear_requirements()

    # 範例 3
    Rq.modify_reqiurements('food', 'french', True)
    Rq.modify_reqiurements('food', 'italian', True)
    Rq.modify_reqiurements('entertainment', 'shopping', True)
    Rq.modify_reqiurements('price', 'low', True)
    Rq.modify_reqiurements('price', 'high', True)
    api.search_reqiurement('3')
    Rq.clear_requirements()


