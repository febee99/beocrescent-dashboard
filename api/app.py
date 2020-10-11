import os, sys
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta
from mongoengine import connect
from models import *

app = Flask(__name__)
CORS(app)

# Mongo Initialization
connect("iot", host="mongodb+srv://root:0NqePorN2WDm7xYc@cluster0.fvp4p.mongodb.net/iot?retryWrites=true&w=majority")


@app.route('/table/<table>')
def get_table(table):
    # error handling not done, the get method will result in error if id not found
    table = Table.objects.get(table=15)

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

@app.route('/table/<table>', methods=['PUT'])
def update_table_state(table):
    state = int(request.args.get('state'))
    table = Table.objects.get(table=15)
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)