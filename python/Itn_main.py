import responses
import googlemaps
from datetime import datetime
import json

import Itn_api as api

if __name__ == '__main__':
    result = api.search_onkey()
    # with open('./test/test1.txt', 'w') as f:
    #     f.write(result)

