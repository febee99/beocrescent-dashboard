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
tray_in_data = db["tray_in_updated"]

@app.route("/rfid_fsr", methods=['GET'])
def rfid_fsr():
    data = collection.find()
    dict_info = {}
    list_data = {'06:00':0, '07:00':0, '08:00':0, '09:00':0, '10:00':0, '11:00':0, '12:00':0, '13:00':0, '14:00':0, '15:00':0, '16:00':0, '17:00':0, '18:00':0, '19:00':0, '20:00':0, "21:00":0, "22:00":0, "23:00":0}
    for single_data in data:
        fsr_status = single_data["fsr_status"]
        timestamp = str(single_data["timestamp"])
        rfid_status = single_data["rfid_status"]
        date = timestamp.split(" ")[0]
        time = timestamp.split(" ")[1][:5]
        if date in dict_info:
            temp_dict = dict_info[date]
            extracted_time = time[0:2] + ":00"
            counttime = temp_dict[extracted_time] 
            counttime += 1
            temp_dict[extracted_time] = counttime
        else:
            dict_info[date] = {'06:00':0, '07:00':0, '08:00':0, '09:00':0, '10:00':0, '11:00':0, '12:00':0, '13:00':0, '14:00':0, '15:00':0, '16:00':0, '17:00':0, '18:00':0, '19:00':0, '20:00':0, "21:00":0, "22:00":0, "23:00":0}
            extracted_time = time[0:2] + ":00"
            list_data[extracted_time] = 1
    print(dict_info)
    return json.dumps(dict_info), 200

@app.route("/tray_in", methods=["GET"])
def tray_in():
    data = tray_in_data.find()
    dict_info = {}
    list_data = {'06:00':0, '07:00':0, '08:00':0, '09:00':0, '10:00':0, '11:00':0, '12:00':0, '13:00':0, '14:00':0, '15:00':0, '16:00':0, '17:00':0, '18:00':0, '19:00':0, '20:00':0, "21:00":0, "22:00":0, "23:00":0}
    for single_data in data:
        print(single_data)
        status_count = single_data["status_count"]
        timestamp = str(single_data["timestamp"])
        date = timestamp.split(" ")[0]
        time = timestamp.split(" ")[1][:5]
        if date in dict_info:
            temp_dict = dict_info[date]
            extracted_time = time[0:2] + ":00"
            counttime = temp_dict[extracted_time] 
            counttime += status_count
            temp_dict[extracted_time] = counttime
        else:
            dict_info[date] = {'06:00':0, '07:00':0, '08:00':0, '09:00':0, '10:00':0, '11:00':0, '12:00':0, '13:00':0, '14:00':0, '15:00':0, '16:00':0, '17:00':0, '18:00':0, '19:00':0, '20:00':0, "21:00":0, "22:00":0, "23:00":0}
            extracted_time = time[0:2] + ":00"
            list_data[extracted_time] = status_count
    return json.dumps(dict_info), 200


@app.route("/tray_in_out", methods=['GET'])
def tray_in_out():
    total_out = collection.find().count() 
    trolley_in = tray_in_data.find()
    total = 0
    for data1 in trolley_in:
        total += data1['status_count']
    self_in = total_out - total
    data = {"CleanerReturn": total, "SelfReturn": self_in}
    return json.dumps(data), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)