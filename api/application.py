import os, sys
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta
from mongoengine import connect
from models import *
from bson.json_util import dumps
import pymongo
import json

app = Flask(__name__)
CORS(app)

# TODO: Put into environment variable
# Mongo Initialization for G7-TableVision
connect("iot", host="mongodb+srv://root:0NqePorN2WDm7xYc@cluster0.fvp4p.mongodb.net/iot?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")

# Mongo Initialization for G7-TrayInOut
g7_client = pymongo.MongoClient("mongodb+srv://root:0NqePorN2WDm7xYc@cluster0.fvp4p.mongodb.net/iot?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")

# Mongo Initialization for G6-TrayInOut
g6_client = pymongo.MongoClient("mongodb+srv://iotadmin:iotadminpassword@cluster0.cowqf.mongodb.net/iotTest?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")

# G7 Initialization
g7_tray_out = g7_client['fsr_rfid']['collection']
g7_tray_in = g7_client['fsr_rfid']['tray_in_updated']
g7_tablevision = g7_client['iot']['session_clean']

# G6 Initialization
positivetrayreturn = g6_client['iotTest']['positivetrayreturn']
stall_distribution = g6_client['iotTest']['stall_distribution']
empty_trayreturn = g6_client['iotTest']['empty_trayreturn']


#! G7 - TABLEVISION
# ===================================================================================================
@app.route('/tables/<table>')
def get_table(table):
    try:
        # error handling not done, the get method will result in error if id not found
        table = Table.objects.get(table=table)

        # currently returning the state integer
        # 0 - vacant
        # 1 - vacant but uncleared
        # 2 - occupied
        print(table.state)

        result = {
            "table": table.table,
            "state": table.state
        }

        return jsonify(result), 200
    except Exception as e:
        return jsonify({
            "type": "error",
            "message": str(e)
        }), 500

@app.route('/tables/<table>', methods=['PUT'])
def update_table_state(table):
    state = int(request.args.get('state'))
    table = Table.objects.get(table=table)
    table.update(set__state=state)

    result = {
        "table": table.table,
        "state": state
    }

    return jsonify(result), 201

@app.route('/tables')
def get_all_tables():
    result = []
    tables = Table.objects()
    
    for table in tables:
        result.append({
            "table": table.table,
            "state": table.state
        })

    result = {
        "tables": result
    }

    return jsonify(result), 200

@app.route('/stats')
def get_return_stats():
    sessions = Session.objects

    cleaner_count = 0
    self_count = 0
    for session in sessions:
        if session.sessionEnd is not None:
            states = session.states
            if states[-2] == 1:
                cleaner_count += 1
            else:
                self_count += 1
    


    # stats = Stat.objects[0]
    # self = stats.selfReturn
    # cleaner = stats.cleanerReturn
    total = self_count + cleaner_count
    if total == 0:
        result = {
            "self": 0,
            "cleaner": 0
        }

        return jsonify(result), 200

    result = {
        "self": round(((self_count / total) * 100), 2),
        "cleaner": round(((cleaner_count / total) * 100), 2),
        "total": total
    }

    return jsonify(result), 200


@app.route('/stats/<dt>')
def get_return_stats_dt(dt):
    # format should be dd-mm-yyyy
    sessions = Session.objects
    # the_date = (datetime.now() + timedelta(hours=8)).date()
    the_date_object = datetime.strptime(dt, '%d-%m-%Y')
    the_date = (the_date_object + timedelta(hours=8)).date()

    cleaner_count = 0
    self_count = 0
    for session in sessions:
        if session.sessionEnd is not None and the_date == session.sessionStart.date():
            states = session.states
            if states[-2] == 1:
                cleaner_count += 1
            else:
                self_count += 1
    
    total = self_count + cleaner_count
    if total == 0:
        result = {
            "self": 0,
            "cleaner": 0
        }

        return jsonify(result), 200

    result = {
        "self": round(((self_count / total) * 100), 2),
        "cleaner": round(((cleaner_count / total) * 100), 2),
        "total": total
    }

    return jsonify(result), 200

def hour_formatter(total, hour_dict):
    if total == 0:
        return {
            "total": total
        }

    return {
        "true_self_count": hour_dict["self_count"],
        "true_cleaner_count": hour_dict["cleaner_count"],
        "self_count": round(((hour_dict["self_count"] / total) * 100), 2),
        "cleaner_count": round(((hour_dict["cleaner_count"] / total) * 100), 2),
        "total": total
    }

@app.route('/stats/per_hour/<dt>')
def get_return_stats_hour_day(dt):
    try:
        # format should be dd-mm-yyyy
        sessions = Session.objects
        # the_date = (datetime.now() + timedelta(hours=8)).date()
        the_date_object = datetime.strptime(dt, '%d-%m-%Y')
        the_date = (the_date_object + timedelta(hours=8)).date()

        hours = {
            "6": {"self_count": 0, "cleaner_count": 0, "total": 0},
            "7": {"self_count": 0, "cleaner_count": 0, "total": 0},
            "8": {"self_count": 0, "cleaner_count": 0, "total": 0},
            "9": {"self_count": 0, "cleaner_count": 0, "total": 0},
            "10": {"self_count": 0, "cleaner_count": 0, "total": 0},
            "11": {"self_count": 0, "cleaner_count": 0, "total": 0},
            "12": {"self_count": 0, "cleaner_count": 0, "total": 0},
            "13": {"self_count": 0, "cleaner_count": 0, "total": 0},
            "14": {"self_count": 0, "cleaner_count": 0, "total": 0},
            "15": {"self_count": 0, "cleaner_count": 0, "total": 0},
            "16": {"self_count": 0, "cleaner_count": 0, "total": 0},
            "17": {"self_count": 0, "cleaner_count": 0, "total": 0},
            "18": {"self_count": 0, "cleaner_count": 0, "total": 0},
            "19": {"self_count": 0, "cleaner_count": 0, "total": 0},
            "20": {"self_count": 0, "cleaner_count": 0, "total": 0}
        }
            
        for session in sessions:
            if session.sessionEnd is not None and the_date == session.sessionStart.date():
                session_hour = str(session.sessionEnd.hour)
                if session_hour in hours:
                    states = session.states
                    if states[-2] == 1:
                        hours[session_hour]["cleaner_count"] += 1
                    else:
                        hours[session_hour]["self_count"] += 1
                    hours[session_hour]["total"] += 1

        for hour in hours:
            hours[hour] = hour_formatter(hours[hour]["total"], hours[hour])

        return jsonify(hours), 200
    except Exception as e:
        return ({
            "type": "error",
            "message": str(e)
        }), 500


@app.route('/distribution')
def distribution():
    sessions = g7_tablevision.find()
    positive_sessions = 0
    negative_sessions = 0
    positive_list = [0] * 4
    negative_list = [0] * 4

    for session in sessions:
        tray_count = session['tray_count']
        if session['states'][-2] == 1:
            negative_sessions += 1
            
            negative_list[tray_count-1] += 1
        else:
            positive_sessions += 1
            positive_list[tray_count-1] += 1

    for i in range(4):
        positive_list[i] = round((positive_list[i]/positive_sessions)*100, 2)
        negative_list[i] = round((negative_list[i]/negative_sessions)*100, 2)

    result = {
        "positive": positive_list,
        "negative": negative_list
    }


    return jsonify(result), 200

# ===================================================================================================

#! G7 - TRAYINOUT
# ===================================================================================================
@app.route("/rfid_fsr", methods=['GET'])
def rfid_fsr():
    data = g7_tray_out.find()
    dict_info = {}
    list_data = {'04:00': 0, '05:00':0, '06:00':0, '07:00':0, '08:00':0, '09:00':0, '10:00':0, '11:00':0, '12:00':0, '13:00':0, '14:00':0, '15:00':0, '16:00':0, '17:00':0, '18:00':0, '19:00':0, '20:00':0, "21:00":0, "22:00":0, "23:00":0}
    for single_data in data:
        fsr_status = single_data["fsr_status"]
        timestamp = str(single_data["timestamp"])
        rfid_status = single_data["rfid_status"]
        date = timestamp.split(" ")[0]
        date = date.split("-")
        if date[2][0] == "0":
            date = date[0] + "-" + date[1] + "-" + date[2][1:]
        else:
            date = date[0] + "-" + date[1] + "-" + date[2]
        time = timestamp.split(" ")[1][:5]
        if date in dict_info:
            temp_dict = dict_info[date]
            extracted_time = time[0:2] + ":00"
            counttime = temp_dict[extracted_time] 
            counttime += 1
            temp_dict[extracted_time] = counttime
        else:
            dict_info[date] = {'04:00':0, '05:00':0, '06:00':0, '07:00':0, '08:00':0, '09:00':0, '10:00':0, '11:00':0, '12:00':0, '13:00':0, '14:00':0, '15:00':0, '16:00':0, '17:00':0, '18:00':0, '19:00':0, '20:00':0, "21:00":0, "22:00":0, "23:00":0}
            extracted_time = time[0:2] + ":00"
            list_data[extracted_time] = 1
    return json.dumps(dict_info), 200

@app.route("/tray_in", methods=["GET"])
def tray_in():
    data = g7_tray_in.find()
    dict_info = {}
    list_data = {'04:00': 0, '05:00':0,'06:00':0, '07:00':0, '08:00':0, '09:00':0, '10:00':0, '11:00':0, '12:00':0, '13:00':0, '14:00':0, '15:00':0, '16:00':0, '17:00':0, '18:00':0, '19:00':0, '20:00':0, "21:00":0, "22:00":0, "23:00":0}
    for single_data in data:
        status_count = single_data["status_count"]
        timestamp = str(single_data["timestamp"])
        date = timestamp.split(" ")[0]
        time = timestamp.split(" ")[1][:5]
        date = date.split("-")
        if date[2][0] == "0":
            date = date[0] + "-" + date[1] + "-" + date[2][1:]
        else:
            date = date[0] + "-" + date[1] + "-" + date[2]
        if date in dict_info:
            temp_dict = dict_info[date]
            extracted_time = time[0:2] + ":00"
            counttime = temp_dict[extracted_time] 
            counttime += status_count
            temp_dict[extracted_time] = counttime
        else:
            dict_info[date] = {'04:00': 0, '05:00':0,'06:00':0, '07:00':0, '08:00':0, '09:00':0, '10:00':0, '11:00':0, '12:00':0, '13:00':0, '14:00':0, '15:00':0, '16:00':0, '17:00':0, '18:00':0, '19:00':0, '20:00':0, "21:00":0, "22:00":0, "23:00":0}
            extracted_time = time[0:2] + ":00"
            list_data[extracted_time] = status_count
    return json.dumps(dict_info), 200


@app.route("/tray_in_out", methods=['GET'])
def tray_in_out():
    total_out = g7_tray_out.find().count() 
    trolley_in = g7_tray_in.find()
    total = 0
    for data1 in trolley_in:
        total += data1['status_count']
    self_in = total_out - total
    data = {"CleanerReturn": total, "SelfReturn": self_in}
    return json.dumps(data), 200

# ===================================================================================================

#! G6
# ===================================================================================================
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

@app.route("/g6barchart", methods=['GET'])
def g6barchart_traydistr():
    data = {"returns": {"2020-10-19":0 , "2020-10-23":0, "2020-10-26":0, "2020-11-07":0}, 
    "distr": {"2020-10-19":0 , "2020-10-23":0, "2020-10-26":0, "2020-11-07":0}}
    distr = stall_distribution.find({"rasp_id": 1})
    returns = positivetrayreturn.find({"stall_id": 1})
    for x in distr:
        d = str(x["datetime"])
        date = d[:10]
        if date in data["distr"]:
            count = data["distr"][date]
            count += 1
            data["distr"][date] = count
    for x in returns:
        d = str(x["datetime"])
        date = d[:10]
        if date in data["returns"]:
            count = data["returns"][date]
            count += 1
            data["returns"][date] = count
    return json.dumps(data), 200
# ===================================================================================================


#! Overview
# ===================================================================================================
@app.route("/overview/tray_return", methods=['GET'])
def overview_tr():
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
    # print(list_data)

    # G7 turn
    tray_out_datas = g7_tray_out.find()
    tray_in_datas = g7_tray_in.find()
    list_of_tray_out = [0] * 20
    list_of_tray_in = [0] * 20
    for data in tray_out_datas:
        data_time = str(data['timestamp']).split()[1][:3] + "00"
        tray_out_index = list_of_time.index(data_time)
        list_of_tray_out[tray_out_index] += 1

    for data in tray_in_datas:
        data_time = str(data['timestamp']).split()[1][:3] + "00"
        tray_in_index = list_of_time.index(data_time)
        list_of_tray_in[tray_in_index] += 1

    list_data2 = {'04:00': 0.00, '05:00': 0.00, '06:00': 0.00, '07:00': 0.00, '08:00': 0.00, '09:00': 0.00, '10:00': 0.00, '11:00': 0.00, 
                '12:00': 0.00, '13:00': 0.00, '14:00': 0.00,'15:00': 0.00, '16:00': 0.00, '17:00': 0.00, '18:00': 0.00, '19:00': 0.00,
                '20:00': 0.00, '21:00': 0.00, '22:00': 0.00, '23:00': 0.00}
    
    for i, t in enumerate(list_of_time):
        try:
            list_data2[t] = round(( (list_of_tray_out[i] - list_of_tray_in[i]) / list_of_tray_out[i])*100, 2)
            if list_data2[t] < 0:
                list_data2[t] = 0
        except:
            continue

    list_data3 = {'04:00': 0.00, '05:00': 0.00, '06:00': 0.00, '07:00': 0.00, '08:00': 0.00, '09:00': 0.00, '10:00': 0.00, '11:00': 0.00, 
                '12:00': 0.00, '13:00': 0.00, '14:00': 0.00,'15:00': 0.00, '16:00': 0.00, '17:00': 0.00, '18:00': 0.00, '19:00': 0.00,
                '20:00': 0.00, '21:00': 0.00, '22:00': 0.00, '23:00': 0.00}

    sessions = g7_tablevision.find()
    list_of_tv_sessions = [0] * 20
    list_of_tv_self_return = [0] * 20

    for session in sessions:
        data_time = str(session['sessionEnd']).split()[1][:3] + "00"
        try:
            index = list_of_time.index(data_time)
        except:
            continue
        
        list_of_tv_sessions[index] += 1

        if session['states'][-2] == 2:
            list_of_tv_self_return[index] += 1

    for i, t in enumerate(list_of_time):
        try:
            list_data3[t] = round((list_of_tv_self_return[i] / list_of_tv_sessions[i])*100, 2)
        except:
            continue
    
    result = {
        'g6': list_data,
        'g7-tray': list_data2,
        'g7-tablevision': list_data3
    }
    

    return jsonify(result), 200

@app.route("/overview2", methods=['GET'])
def overview2():
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

    totalreturn = 0
    totaldistr = 0
    for key, value in data['returns'].items():
        totalreturn += value

    for key, value in data['distr'].items():
        totaldistr += value

    g6 = round( (totalreturn/totaldistr) *100, 2)

    # G7 tablevision
    sessions = g7_tablevision.find()
    total_sessions = g7_tablevision.find().count()
    positive_sessions = 0
    sessions = g7_tablevision.find()

    for session in sessions:
        if session['states'][-2] == 2:
            positive_sessions += 1

    g7tb = round( (positive_sessions/total_sessions) *100, 2)


    # G7 tray return
    total_out = g7_tray_out.find().count() 
    trolley_in = g7_tray_in.find()
    total = 0
    for data1 in trolley_in:
        total += data1['status_count']
    self_in = total_out - total
    data = {"CleanerReturn": total, "SelfReturn": self_in}

    g7tr = round((self_in / total_out)*100, 2)

    result = {
        'g6': g6,
        'g7tb': g7tb,
        'g7tr': g7tr,
    }
    return jsonify(result), 200

    # return str(round( (totalreturn/totaldistr) *100, 2)), 200

# TODO: Tablevision distribution stats

# ===================================================================================================

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)