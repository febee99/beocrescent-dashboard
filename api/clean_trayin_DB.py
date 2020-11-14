import pymongo
from datetime import datetime

import json

client = pymongo.MongoClient("mongodb+srv://root:0NqePorN2WDm7xYc@cluster0.fvp4p.mongodb.net/iot?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")

db = client['fsr_rfid']
tray_in_data = db["tray_in"]

##Remove Incorrect Data
def cleanData(tray_in_data, db_name):
    for i in range(tray_in_data.find().count()-1):
        current_data = tray_in_data.find()[i]
        current_datetime = current_data["timestamp"]
        next_data = tray_in_data.find()[i+1]
        next_datetime = next_data["timestamp"]
        difference = next_datetime - current_datetime
        duration = difference.seconds
        if duration >= 60:
            db_name.insert_one(tray_in_data.find()[i])


db_name = client.fsr_rfid.tray_in_updated
cleanData(tray_in_data, db_name)


        
