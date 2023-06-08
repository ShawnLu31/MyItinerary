import googlemaps
import Itn_keyword as kw
import Itn_function as Fc
import Itn_database as Db
import json

gmaps = googlemaps.Client(key=kw.API_KEY)

attr = []
hotel = []
# {'place_name':"臺南市美術館2館", 
#          'place_id':"ChIJQW7Ewnx2bjQR2vkI8YSRFXM",
#          'cost': 200 },
#          {'place_name':"安平樹屋", 
#           'place_id':"ChIJlynOByF3bjQR_IzNSlgH-Ss",
#           'cost': 70},

name_list = ['臺南市美術館2館', 
             '臺南市美術館1館',
             '安平樹屋', 
             '奇美博物館',
             '河樂廣場',
             '安平古堡',
             '關子嶺溫泉老街',
             '四草綠色隧道',
             '漁光島',
             '麻豆代天府',
             '鹿耳門天后宮',
             '七股鹽山',
             '國立臺灣文學館',
             '臺灣祀典武廟',
             '臺南文化創意產業園區',
             '國華街',
             '神農街',
             '延平郡王祠',
             '二鯤鯓砲臺(億載金城)',         
             '南紡購物中心',
             '新光三越台南新天地',
             '藍晒圖文創園區']

hotel_list = ['煙波大飯店台南館',
              '台南晶英酒店',
              'UIJ Hotel & Hostel - 友愛街旅館',
              '泊樂行旅',
              '巷弄潮旅',
              '仲青行旅台南館',
              '台南長悅旅棧',
              '康橋商旅赤崁樓',
              '富信大飯店',
              '台南老爺行旅',
              '香格里拉台南遠東國際大飯店',
              '台糖長榮酒店',
              '湧福驛站',
              '漫半拍',
              '一緒二咖啡民居'
              ]    

db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "ncku2023",
    "db": "itinerary",
    "charset": "utf8"
}

table_name_list = ['attractions', 'hotels']

def find_id():
    result = gmaps.places_autocomplete(
        input_text=name_list[0],
        language='zh-TW'
    )
#     id = gmaps.place(
#              place_id="ChIJbYl7d2F2bjQRnFdvyMBuZfI",
#              fields=['geometry/location'],
#              language='zh-TW',
#     )
    for name in name_list:
        result = gmaps.places_autocomplete(
                input_text=name,
                language='zh-TW'
        )
        p_name = result[0]['structured_formatting']['main_text']
        id = result[0]['place_id']
        attr.append({'place_name': p_name, 'place_id': id, 'cost': 0})

    Fc.dump_json("attr", attr)

    for h in hotel_list:
        result = gmaps.places_autocomplete(
                input_text=h,
                language='zh-TW'
        )
        p_name = result[0]['structured_formatting']['main_text']
        id = result[0]['place_id']
        hotel.append({'place_name': p_name, 'place_id': id, 'cost': 0})

    Fc.dump_json("hotel", hotel)
    
if __name__ == '__main__':
    with open('./test/attr.json', encoding='utf-8') as f:
        data = json.load(f)
    Db.insertData('attractions', data)
    with open('./test/hotel.json', encoding='utf-8') as f:
        data = json.load(f)
    Db.insertData('hotels',data)

