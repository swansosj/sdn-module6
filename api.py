#!/usr/bin/python3

import flask
from flask import Flask
from flask import request, jsonify

app = Flask(__name__)


course = [
    {'id':0,
    'course': 'Software Defined Networking',
    'school': 'Florida State College at Jacksonville',
    'instructor': 'Sheldon Swanson'}
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome SDN World!!!</h1><p>This is an example API service with Flask</p>"

@app.route('/api/all', methods=['GET'])
def api_all():
    return jsonify(course)

if __name__ == '__main__':
    app.run(port=80, debug=True, host='0.0.0.0',)
