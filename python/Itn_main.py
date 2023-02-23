import responses
import googlemaps
from datetime import datetime
import json

import Itn_api as api
import Itn_function as Fc
import Itn_keyword as kw
from Itn_requirements import Requirements 


gmaps = googlemaps.Client(key=kw.API_KEY)

loc = (22.997409807642487, 120.22060180281467)
rad = 500

result = gmaps.places(
    "restaurant",
    location=loc,
    radius=rad,
    language="zh-TW"
    )

with open('data.json', 'w') as f:
    json.dump(result, f)
