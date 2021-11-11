import os
import socket
from flask import Flask, Response, request
from flask_api import status
import ifaddr

app = Flask(__name__)


# @app.route('/me')
# def hello():
#    return '<h1></h1>'


# @app.route('/health/')
# def about():
#    return '<h3>OK</h3>'

@app.route('/me')
def ips():
    result = ""
    for adapter in ifaddr.get_adapters():
        result = result + f'IP addressing of network adapter {adapter.nice_name}\n'
        for ip in adapter.ips:
            result = result + f'  - {ip.ip}/{ip.network_prefix}\n'
    return Response(result, mimetype='text/plain')

# @app.route('/health')
# def ok():
# export ENV=OK
# app.config['ENV'] = environ.get('ENV')
