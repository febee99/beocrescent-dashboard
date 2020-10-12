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
collection = db['positivetrayreturn']


@app.route("/g6trayreturn", methods=['GET'])
def g6trayreturn():
    list_of_time = ['06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00',
                    '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00']
    dict_info = {}
    list_data = {'06:00': 0, '07:00': 0, '08:00': 0, '09:00': 0, '10:00': 0, '11:00': 0, '12:00': 0, '13:00': 0, '14:00': 0,
                 '15:00': 0, '16:00': 0, '17:00': 0, '18:00': 0, '19:00': 0, '20:00': 0, "21:00": 0, "22:00": 0, "23:00": 0}
    data = collection.find()
    for x in data:
        print(x)
        datetime = str(x["datetime"])
        d = datetime.replace(",", "-")
        date = d[:10]
        time = d[11:13] + ":00"
        dict_info[date] = list_data
        if date in dict_info:
            print(date)
            temp_dict = dict_info[date]
            counttime = temp_dict[time]
            counttime += 1
            temp_dict[time] = counttime
        else:
            dict_info[date] = list_data
        print(dict_info)
    return json.dumps(dict_info), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
