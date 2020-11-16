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
empty_trayreturn = db['empty_trayreturn']

@app.route("/g6trayreturndistr/<stall_id>/<date_wanted>", methods=['GET'])
def g6trayreturndistr(stall_id, date_wanted):
    list_data = {"returns": {'06:00': 0, '07:00': 0, '08:00': 0, '09:00': 0, '10:00': 0, '11:00': 0, '12:00': 0, '13:00': 0, '14:00': 0,
                 '15:00': 0, '16:00': 0, '17:00': 0, '18:00': 0, '19:00': 0, '20:00': 0, "21:00": 0, "22:00": 0, "23:00": 0},
                 "distr": {'06:00': 0, '07:00': 0, '08:00': 0, '09:00': 0, '10:00': 0, '11:00': 0, '12:00': 0, '13:00': 0, '14:00': 0,
                 '15:00': 0, '16:00': 0, '17:00': 0, '18:00': 0, '19:00': 0, '20:00': 0, "21:00": 0, "22:00": 0, "23:00": 0}}
    data = positivetrayreturn.find({"stall_id": int(stall_id)})
    for x in data:
        d = str(x["datetime"])
        date = d[:10]
        if date == date_wanted:
            time = d[11:13] + ":00"
            counttime = list_data["returns"][time]
            counttime += 1
            list_data["returns"][time] = counttime
    print(list_data)

    data2 = stall_distribution.find({"rasp_id": int(stall_id)})
    for x in data2:
        d = str(x["datetime"])
        date = d[:10]
        if date == date_wanted:
            time = d[11:13] + ":00"
            counttime = list_data["distr"][time]
            counttime += 1
            list_data["distr"][time] = counttime
    print(list_data)
    return json.dumps(list_data), 200

@app.route("/g6trayclear/<date_wanted>", methods=['GET'])
def g6trayclear(date_wanted):
    count = 0
    data = empty_trayreturn.find()
    for x in data:
        d = str(x["datetime"])
        date = d[:10]
        if date == date_wanted:
            count += 1
    
    data = {"Cleared": count} 
    print(data)
    return json.dumps(data), 200

@app.route("/g6total/<stall_id>/<date_wanted>", methods=['GET'])
def g6total(stall_id, date_wanted):
    total_distr = 0
    data = stall_distribution.find({"rasp_id": int(stall_id)})

    for x in data:
        d = str(x["datetime"])
        date = d[:10]
        if date == date_wanted:
            total_distr += 1

    total_return = 0
    data2 = positivetrayreturn.find({"stall_id": int(stall_id)})
    for y in data2:
        d = str(y["datetime"])
        date = d[:10]
        if date == date_wanted:
            total_return += 1

    clear_count = 0
    data3 = empty_trayreturn.find()
    for y in data3:
        d = str(y["datetime"])
        date = d[:10]
        if date == date_wanted:
            clear_count += 1

    not_returned = total_distr - total_return 
    data = {"NotReturned": not_returned , "Returned": total_return, "Cleared": clear_count}
    print(data)
    return json.dumps(data), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
