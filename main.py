# -*- coding: utf-8 -*-
#!flask/bin/python
from flask import Flask, jsonify, request, make_response
import requests

app = Flask(__name__)

url_set = ['http://lixichcska.pythonanywhere.com/', 'http://lixichamkar.pythonanywhere.com/']
last_seconds = 1.0

@app.route('/<path:path>', methods = ['GET', 'PUT', 'POST', 'DELETE'])
def home(path):
    min_url = ''
    min_perf = 10000
    for url in url_set:
        try:
            perf = requests.get(url + 'metrics/' + str(last_seconds)).json()['AverageResponseTime']
            if float(perf) < min_perf:
                min_url = url
                min_perf = perf
        except:
            pass
    if min_url == '':
        print('No servers available')
        return make_response(jsonify({'Error': 'No servers available'}), 404)
    print(str(min_url+path), request.method, request.json)
    if request.method =='GET':
        return jsonify(requests.get(min_url + path).json())
    elif request.method =='DELETE':
        return jsonify(requests.delete(min_url + path).json())
    elif request.method =='PUT':
        return jsonify(requests.put(min_url + path, json=request.json).json())
    elif request.method =='POST':
        return jsonify(requests.post(min_url + path, json=request.json).json())

if __name__ == '__main__':
    app.run(threaded=True, debug=True)
