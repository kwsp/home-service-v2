"""
Legacy script that migrates the base64 encoded text database
to a SQLite3 database
"""
import glob
import struct
import binascii
from datetime import datetime
import sqlite3
import os
import sys

# Safety check
res = input(
    "This script should only be run once to" + "convert txt to db. Proceed? (Y/[N]) "
)
if res == "" or res == "N" or res == "n":
    sys.exit()


def unpack(fmat, data, index):
    unpackedStuff = struct.unpack_from(fmat, data, index)
    index += struct.Struct(fmat).size
    return idx, unpackedStuff


# Get DB path
db_name = "tiger-home.db"
db_path = os.path.join(os.getcwd(), "data", db_name)

# Create the DB
connection = sqlite3.connect(db_path)
c = connection.cursor()

c.execute(
    """CREATE TABLE sensor_data
             (timestamp integer, temperature real, activity integer)"""
)

c.execute("SELECT * FROM sensor_data")
temp = c.fetchall()
print("[BEFORE] DB has {} entries".format(len(temp)))

# Get .txt files
files = glob.glob("data/*.txt")
files.sort()


for inFileName in files:
    inFile = open(inFileName, "rb")

    # Batch insert
    records = []
    for i, line in enumerate(inFile):
        data = binascii.a2b_base64(line)
        idx = 0
        idx, (time, temp, acti) = unpack("<IfI", data, idx)

        records.append((time, round(temp, 2), acti))

    c.executemany("INSERT INTO sensor_data VALUES (?,?,?)", records)

connection.commit()

c.execute("SELECT * FROM sensor_data")
temp = c.fetchall()
print("[AFTER] DB has {} entries".format(len(temp)))
