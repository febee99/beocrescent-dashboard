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


@app.route("/g6trayreturn//<stall_id>/<date_wanted>", methods=['GET'])
def g6trayreturn(stall_id, date_wanted):
    list_of_time = ['06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00',
                    '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00']
    list_data = {'06:00': 0, '07:00': 0, '08:00': 0, '09:00': 0, '10:00': 0, '11:00': 0, '12:00': 0, '13:00': 0, '14:00': 0,
                 '15:00': 0, '16:00': 0, '17:00': 0, '18:00': 0, '19:00': 0, '20:00': 0, "21:00": 0, "22:00": 0, "23:00": 0}
    data = positivetrayreturn.find({"stall_id": int(stall_id)})
    for x in data:
        datetime = str(x["datetime"])
        d = datetime.replace(",", "-")
        date = d[:10]
        if date == date_wanted:
            time = d[11:13] + ":00"
            counttime = list_data[time]
            counttime += 1
            list_data[time] = counttime
    print(list_data)
    return json.dumps(list_data), 200


@ app.route("/g6traydistr/<stall_id>/<date_wanted>", methods=['GET'])
def g6traydistr(stall_id, date_wanted):
    list_of_time = ['06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00',
                    '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00']
    list_data = {'06:00': 0, '07:00': 0, '08:00': 0, '09:00': 0, '10:00': 0, '11:00': 0, '12:00': 0, '13:00': 0, '14:00': 0,
                 '15:00': 0, '16:00': 0, '17:00': 0, '18:00': 0, '19:00': 0, '20:00': 0, "21:00": 0, "22:00": 0, "23:00": 0}
    data = stall_distribution.find({"rasp_id": int(stall_id)})

    for x in data:
        datetime = str(x["datetime"])
        d = datetime.replace(",", "-")
        date = d[:10]
        if date == date_wanted:
            time = d[11:13] + ":00"
            counttime = list_data[time]
            counttime += 1
            list_data[time] = counttime
    print(list_data)
    return json.dumps(list_data), 200


@app.route("/g6total/<stall_id>/<date_wanted>", methods=['GET'])
def g6total(stall_id, date_wanted):
    total_distr = 0
    data = stall_distribution.find({"rasp_id": int(stall_id)})
    for x in data:
        datetime = str(x["datetime"])
        d = datetime.replace(",", "-")
        date = d[:10]
        if date == date_wanted:
            total_distr += 1

    total_return = 0
    data2 = positivetrayreturn.find({"stall_id": int(stall_id)})
    for y in data2:
        datetime = str(y["datetime"])
        d = datetime.replace(",", "-")
        date = d[:10]
        if date == date_wanted:
            total_return += 1

    not_returned = total_distr - total_return
    data = {"NotReturned": not_returned, "Returned": total_return}
    print(data)
    return json.dumps(data), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
