from datetime import datetime
import time
import os
from get_db import db


connection = db()
c = connection.cursor()

c.execute("SELECT * FROM sensor_data ORDER BY timestamp DESC LIMIT 10")
res = c.fetchall()
print("Latest sensor_data:")
for r in res:
    t = datetime.fromtimestamp(r[0])
    print("Time: ", t, " TempC: ", round(r[1], 2), " Acti:", r[2])

c.execute("SELECT * FROM pi_temp ORDER BY timestamp DESC LIMIT 10")
res = c.fetchall()
print("Latest pi_temp:")
for r in res:
    t = datetime.fromtimestamp(r[1])
    print("Name: ", r[0], "Time: ", t, " TempC: ", r[2])


c.close()
connection.close()
