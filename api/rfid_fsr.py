from flask import Flask, jsonify, request
import pymongo
from flask_cors import CORS
from os import environ
from bson.json_util import dumps

import json

app = Flask(__name__)
client = pymongo.MongoClient("mongodb+srv://root:0NqePorN2WDm7xYc@cluster0.fvp4p.mongodb.net/iot?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")

CORS(app)

db = client['fsr_rfid']
collection = db['collection']

@app.route("/rfid_fsr", methods=['GET'])
def rfid_fsr():
    data = collection.find()
    print(data)
    return dumps(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)