# -*- coding: utf-8 -*-
#!flask/bin/python
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

url_set = ['http://aachusovlyankin.pythonanywhere.com/', 'http://lixichcska.pythonanywhere.com/']
las_seconds = 60

@app.route('/<path:path>', methods = ['GET', 'PUT', 'POST', 'DELETE'])
def home(path):
    min_url = url_set[0]
    min_perf = requests.get(min_url + 'metrics/' + str(las_seconds)).json()['AverageResponseTime']
    for url in url_set[1:]:
        perf = requests.get(url + 'metrics/' + str(las_seconds)).json()['AverageResponseTime']
        if float(perf) < min_perf:
            min_url = url
            min_perf = perf
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
    app.run(debug=True)
