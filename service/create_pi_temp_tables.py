from datetime import datetime
import sqlite3
import os

import get_db

# Connect
con = get_db.db()
c = con.cursor()

c.execute('''CREATE TABLE pi_temp
             (name TEXT, timestamp INTEGER, temperature REAL)''')

c.execute("SELECT * FROM pi_temp")
temp = c.fetchall()
print("Currently pi_temp has: ")
print(temp)
