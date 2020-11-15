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

@app.route("/g6overview", methods=['GET'])
def g6total():
    list_of_time = ['04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00',
                    '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
    list_data = {'04:00': 0.00, '05:00': 0.00, '06:00': 0.00, '07:00': 0.00, '08:00': 0.00, '09:00': 0.00, '10:00': 0.00, '11:00': 0.00, 
                '12:00': 0.00, '13:00': 0.00, '14:00': 0.00,'15:00': 0.00, '16:00': 0.00, '17:00': 0.00, '18:00': 0.00, '19:00': 0.00,
                '20:00': 0.00, '21:00': 0.00, '22:00': 0.00, '23:00': 0.00}
    distr_data = {'04:00': 0, '05:00': 0, '06:00': 0, '07:00': 0, '08:00': 0, '09:00': 0, '10:00': 0, '11:00': 0, 
                '12:00': 0, '13:00': 0, '14:00': 0,'15:00': 0, '16:00': 0, '17:00': 0, '18:00': 0, '19:00': 0,
                '20:00': 0, '21:00': 0, '22:00': 0, '23:00': 0}
    return_data = {'04:00': 0, '05:00': 0, '06:00': 0, '07:00': 0, '08:00': 0, '09:00': 0, '10:00': 0, '11:00': 0, 
                '12:00': 0, '13:00': 0, '14:00': 0,'15:00': 0, '16:00': 0, '17:00': 0, '18:00': 0, '19:00': 0,
                '20:00': 0, '21:00': 0, '22:00': 0, '23:00': 0}                          
    distr = stall_distribution.find({"rasp_id": 1})
    ptr = positivetrayreturn.find({"stall_id": 1})
    for x in distr:
        datetime = str(x["datetime"])
        d = datetime.replace(",", "-")
        date = d[:10]
        time = d[11:13] + ":00"
        counttime = distr_data[time]
        counttime += 1
        distr_data[time] = counttime
    for x in ptr:
        datetime = str(x["datetime"])
        d = datetime.replace(",", "-")
        date = d[:10]
        time = d[11:13] + ":00"
        counttime = return_data[time]
        counttime += 1
        return_data[time] = counttime
    for y in distr_data:
        for z in return_data:
            if y == z:
                if (distr_data[y] != 0):
                    list_data[y] = return_data[z] / distr_data[y] * 100
    print(list_data)      
    return json.dumps(list_data), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
