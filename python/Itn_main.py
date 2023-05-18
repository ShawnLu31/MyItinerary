from flask import Flask, request, render_template, redirect, url_for
import json

import Itn_search as Srh
import Itn_requirements as Rq 
import placeloc as pl

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('web.html')

    return render_template('web.html')
    

@app.route('/search', methods=['POST'])
def search():
    print("search")
    # Srh.search_reqiurement('2')
    Srh.search_onekey('onekey')
    # pl.get_place_loc()

    return redirect('/')

@app.route('/modify', methods=['POST'])
def modifyRequirements():
    print("modify")
    if request.method == 'POST':
        # get requirement value
        reqs = request.json['requirements']
        print("reqs: ",reqs)
        for rq in reqs:
            Rq.modify_reqiurements(rq, True)

    return redirect('/')

@app.route('/show', methods=['GET'])
def show():
    print("show")
    return redirect(url_for('showPlaceDetail'))

@app.route('/show/place_detail', methods=['GET'])
def showPlaceDetail():
    fname = './test/' + 'resultonekey' +'.json'
    with open(fname, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # deatils
    p1 = {
        'name': data['restaurant']['result']['name'],
        'addr': data['restaurant']['result']['formatted_address'],
        'rating': data['restaurant']['result']['rating']
    }
    p2 = {
        'name': data['attraction']['result']['name'],
        'addr': data['attraction']['result']['formatted_address'],
        'rating': data['attraction']['result']['rating']
    }
    route = {
        'route': data['route'][0]['summary'],

    }
    
    Rq.clear_requirements() #########################

    # show routes on map

    return render_template('web.html', placeInfo1=p1, placeInfo2=p2, routeInfo1=route, initMap=False)

@app.route('/show/map_detail', methods=['GET'])
def showMapInfo():
    fname = './test/' + 'resultonekey' +'.json'
    with open(fname, 'r', encoding='utf-8') as f:
        data = json.load(f)
    mapInfo = {
        'p1': data['restaurant']['result']['place_id'],
        'p2': data['attraction']['result']['place_id']
    }
    print(mapInfo)
    return mapInfo

if __name__ == '__main__':
    app.run(debug=True)
    


