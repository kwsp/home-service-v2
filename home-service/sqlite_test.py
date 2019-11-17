import sqlite3
import os
import time
import random

# Get DB path
db_name = "tiger-home.db"
db_path = os.path.join(os.getcwd(),
                       '../data',
                       db_name)

# Create the DB
connection = sqlite3.connect(db_path)
c = connection.cursor()
# timestamp - integer - unix time
# temperature - real - TempC
# Activity - integer

c.execute('''CREATE TABLE sensor_data
             (timestamp integer, temperature real, activity integer)''')

c.execute('''INSERT INTO sensor_data VALUES
             (1568896927, 23.12, 35)''')

# Look up
c.execute('SELECT * FROM sensor_data')
print(c.fetchall())

# Batch insert
records = []
t = time.time()
for i in range(1000):
    t += 1
    records.append(
        (t, random.randrange(10, 30), random.randrange(10, 30))
    )

c.executemany('INSERT INTO sensor_data VALUES (?,?,?)', records)
