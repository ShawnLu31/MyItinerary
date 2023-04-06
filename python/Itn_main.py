from flask import Flask, request, render_template
import json

import Itn_search as Srh
import Itn_requirements as Rq 

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template('web.html')

@app.route('/search', methods=['POST'])
def search():
    return "search"

@app.route('/modify', methods=['POST'])
def modifyRequirements():
    return "modify"

if __name__ == '__main__':
    app.run(debug=True)
    # # 範例 1
    # Rq.modify_reqiurements('food', 'japanese', True)
    # Rq.modify_reqiurements('price', 'normal', True)
    # Srh.search_reqiurement('1')
    # Rq.clear_requirements()

    # # 範例 2
    # Rq.modify_reqiurements('food', 'fast food', True)
    # Rq.modify_reqiurements('entertainment', 'movie', True)
    # Rq.modify_reqiurements('price', 'low', True)
    # Srh.search_reqiurement('2')
    # Rq.clear_requirements()

    # # 範例 3
    # Rq.modify_reqiurements('food', 'french', True)
    # Rq.modify_reqiurements('food', 'italian', True)
    # Rq.modify_reqiurements('entertainment', 'shopping', True)
    # Rq.modify_reqiurements('price', 'low', True)
    # Rq.modify_reqiurements('price', 'high', True)
    # Srh.search_reqiurement('3')
    # Rq.clear_requirements()


