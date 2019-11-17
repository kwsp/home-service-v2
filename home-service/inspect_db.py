from datetime import datetime
import time
import os
from get_db import db


connection = db()
c = connection.cursor()

c.execute("SELECT * FROM sensor_data ORDER BY timestamp DESC LIMIT 10")
res = c.fetchall()

print("Latest Data:")
for r in res:
    t = datetime.fromtimestamp(r[0])
    print("Time: ", t, " TempC: ", round(r[1], 2), " Acti:", r[2])
