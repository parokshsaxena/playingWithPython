#!/usr/bin/python

from flask import Flask,request
from dao import filterSearch
import json

app = Flask(__name__)

@app.route('/getUser')
def getUserDetails():
    userString = request.args.get('user')
    searchResult = filterSearch(userString)
    return json.dumps(searchResult)
    #return "Hello, World! " + userString

if __name__ == '__main__':
	app.run(debug=True)
