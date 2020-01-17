from datetime import datetime
import sqlite3
import os

import get_db

# Connect
con = get_db.db()
c = con.cursor()


def createPiTemp(c):
    c.execute('''CREATE TABLE IF NOT EXISTS pi_temp
                 (name TEXT, timestamp INTEGER, temperature REAL)''')
    c.execute("SELECT * FROM pi_temp")
    res = c.fetchall()
    print("Currently pi_temp has: ")
    print(res)

def createSensorTempTable(c):
    c.execute('''CREATE TABLE IF NOT EXISTS sensor_temp
                 (name TEXT, timestamp INTEGER, temperature REAL)''')
    c.execute("SELECT * FROM sensor_temp")
    res = c.fetchall()
    print("Currently sensor_temp has: ")
    print(res)

def createSensorHumidityTable(c):
    c.execute('''CREATE TABLE IF NOT EXISTS sensor_humidity
                 (name TEXT, timestamp INTEGER, humidity REAL)''')
    c.execute("SELECT * FROM sensor_humidity")
    res = c.fetchall()
    print("Currently sensor_humidity has: ")
    print(res)

createPiTemp(c)
createSensorTempTable(c)
createSensorHumidityTable(c)
con.commit()
