"""
REST API built using Bottle
"""

from bottle import route, run, response, HTTPResponse
import json
import os

@route('/api/top_100')
def get_top_100():
    # if our file does not exist, return HTTP 500. This will happen if the analysis container was not ran and the results weren't written to it's appropriate location
    top_100_path = '/files/top_100.txt'
    if not os.path.exists(top_100_path):
        return HTTPResponse(status=500, body=json.dumps([{'Error': 'The top 100 file doesn\'t exist yet... Did the analysis container run appropriately?'}])) 

    # read our json stored top 100 and return a successful response
    with open(top_100_path) as f:
        data = f.read()

    response.content_type = 'application/json'
    return HTTPResponse(status=200, body=data)

if __name__ == '__main__':
    run(host='0.0.0.0', port=8001)