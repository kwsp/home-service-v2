import time
import os
import sqlite3
from read_serial import getData
from get_db import db


connection = db()
c = connection.cursor()

# Get data through Serial
raw = getData().split(",")
temperature = raw[0]
activity = raw[1]

# Write to DB
record = (int(time.time()), round(float(temperature), 2), int(activity))
c.execute("INSERT INTO sensor_data VALUES (?,?,?)", record)
connection.commit()
connection.close()
