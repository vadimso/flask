from flask import request
from flask import jsonify
import os
import socket
from flask import Flask, Response, request
import ifaddr

app = Flask(__name__)

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200
