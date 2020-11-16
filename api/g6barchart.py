from flask import Flask, jsonify, request
import pymongo
from flask_cors import CORS
from os import environ
from bson.json_util import dumps

import json

app = Flask(__name__)
client = pymongo.MongoClient(
    "mongodb+srv://iotadmin:iotadminpassword@cluster0.cowqf.mongodb.net/iotTest?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")

CORS(app)

db = client['iotTest']
positivetrayreturn = db['positivetrayreturn']
stall_distribution = db['stall_distribution']

@app.route("/g6barchart", methods=['GET'])
def g6barchart_traydistr():
    data = {"returns": {"2020-10-19":0 , "2020-10-23":0, "2020-10-26":0, "2020-11-07":0}, 
    "distr": {"2020-10-19":0 , "2020-10-23":0, "2020-10-26":0, "2020-11-07":0}}
    distr = stall_distribution.find({"rasp_id": 1})
    returns = positivetrayreturn.find({"stall_id": 1})
    for x in distr:
        datetime = str(x["datetime"])
        d = datetime.replace(",", "-")
        date = d[:10]
        if date in data["distr"]:
            count = data["distr"][date]
            count += 1
            data["distr"][date] = count
    for x in returns:
        datetime = str(x["datetime"])
        d = datetime.replace(",", "-")
        date = d[:10]
        if date in data["returns"]:
            count = data["returns"][date]
            count += 1
            data["returns"][date] = count
    print(data)
    return json.dumps(data), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)
