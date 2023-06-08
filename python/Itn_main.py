from flask import Flask, request, render_template, redirect, url_for
import json

import Itn_search as Srh
import Itn_requirements as Rq 

app = Flask(__name__)
fname = None

@app.route('/',methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('web.html')

    return render_template('web.html')
    

@app.route('/search', methods=['POST'])
def search():
    print("search")
    Srh.search_onekey()

    Rq.clear_requirements() 

    return redirect('/')

@app.route('/modify', methods=['POST'])
def modifyRequirements():
    print("modify")
    if request.method == 'POST':
        # get requirement value
        reqs = request.json['requirements']
        print("reqs: ",reqs)
        for rq in reqs:
            Rq.modify_reqiurements(rq, '1')
        Rq.budget = request.json['budget']
    return redirect('/')

@app.route('/show/place_detail', methods=['POST'])
def showPlaceDetail():
    fname = request.json['fname']
    with open(fname, 'r', encoding='utf-8') as f:
        data = json.load(f)
    detail_content = {
        'attr1_name': data["attr1"]["result"]["name"],
        'food1_name': data["food1"]["result"]["name"],
        'hotel_name': data["hotel"]["result"]["name"] if data['hotel'] is not None else None,
        'attr2_name': data["attr2"]["result"]["name"],
        'food2_name': data["food2"]["result"]["name"],
    }
    
    html_context = f""
    for key, data in detail_content.items():
        if data is not None:
            html_context += f"<div class=\"location-block\"> <h1>{ data }</h1></div>"

    return html_context


@app.route('/show/map_detail/', methods=['POST'])
def showMapInfo():
    fname = request.json['fname']
    print('f', fname)
    with open(fname, 'r', encoding='utf-8') as f:
        data = json.load(f)
    mapInfo = {
        'ori': data['attr1']['result']['place_id'],
        'wayps': [data['food1']['result']['place_id'],
                  data['attr2']['result']['place_id']],
        'des': data['food2']['result']['place_id']
    }
    if  data['hotel'] is not None:
        mapInfo['wayps'].insert(1, data['hotel']['result']['place_id'])
        
    print(mapInfo)
    return mapInfo

if __name__ == '__main__':
    app.run(debug=True)
    


