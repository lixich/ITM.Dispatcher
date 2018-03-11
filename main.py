# -*- coding: utf-8 -*-
#!flask/bin/python
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/<path:path>', methods = ['GET', 'PUT', 'POST', 'DELETE'])
def home(path):
    print(path, request.method)
    return jsonify(requests.get('http://aachusovlyankin.pythonanywhere.com/' + path).json())

if __name__ == '__main__':
    app.run(debug=True)
