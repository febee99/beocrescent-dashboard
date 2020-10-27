import os, sys
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta
from mongoengine import connect
from models import *

app = Flask(__name__)
CORS(app)

# Mongo Initialization
connect("iot", host="mongodb+srv://root:0NqePorN2WDm7xYc@cluster0.fvp4p.mongodb.net/iot?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")


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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)