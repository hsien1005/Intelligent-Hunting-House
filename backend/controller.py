from flask import Flask, request, abort
import json
from flask_cors import CORS
from flask import render_template
from flask import request,jsonify
import pymongo
from bson import json_util
# from lineBot import send_message
# from lineBot import webhook
from db import connectMongo
from db import deleteAllDocuments
from db import getMongo
from db import InsertMongo
import logging
from crawler import *

app = Flask(__name__)
CORS(app)

@app.route("/")
def test_insert():
    try:
        x = getMongo()
        
        return "mongoConnect" 
    except Exception as e:
        return "mongo error {}".format(e)

@app.route("/crawler")
def crawler():
    try:
        data = crawler_591()
        logging.warn(data)
        return "crawler success" 
    except Exception as e:
        return "crawler error {}".format(e)

@app.route("/signUp", methods=['POST'])
def signUp():
    return "sign up post"


@app.route("/login", methods=['POST'])
def login():
    return "login post"

@app.route("/getLove", methods=['GET'])
def getLove():
    return "getLove"

@app.route("/getAll", methods=['GET'])
def getAll():
    x = getMongo()
    return jsonify({"allRoom": x}), 200

@app.route("/getHistory", methods=['GET'])
def getHistory():
    return "getHistory"



@app.route("/postLove", methods=['POST'])
def postLove():
    return "postLove"

@app.route("/postHistory", methods=['POST'])
def postHistory():
    return "postHistory"


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)

# curl -X POST -d "user_id=USER_LINE_ID&message=Hello%20World" http://localhost:5000/send_message 向特定用戶發送訊息
