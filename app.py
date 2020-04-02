# Python SNMP monitoring code for ISOTDAQ Networking Lab
# USAGE:  python app.py
#
# Author: Adam Abed Abud
# Mail: adam.abed.abud@cern.ch
# Last update: May 14, 2019


#!/usr/bin/env python

import json
from time import time
from random import random
from flask import Flask, render_template, make_response
import operator
import sqlite3

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', data='test')

@app.route('/live-data')
def live_data():
    """
    Query the sqlite3 table
    Create an array data = [time() * 1000, PORT_RATES] 
    Output in json format    
    """

    sqlite_file = 'database/switch_monitoringDB.sqlite'    # name of the sqlite database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute("SELECT time, IN_port_1, OUT_port_1, IN_port_3, OUT_port_3, IN_port_13, OUT_port_13, IN_port_15, OUT_port_15 FROM switch_monitor ORDER BY ROWID DESC LIMIT 1")
    data = [[time()*1000, i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]] for i in c.fetchall()]

    print data[0]

    response = make_response(json.dumps(data[0]))  
    response.content_type = 'application/json'
    return response



if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)






