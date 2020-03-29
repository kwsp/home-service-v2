"""
Prints the latest data from home service's sqlite3 database

A path to the database file can be provided as a parameter,
else it will use the default location "~/.home_service/home_service.db"
"""
from datetime import datetime
import sqlite3
import pathlib
import sys


def print_latest_data(db_path):
    connection = sqlite3.connect(db_path)
    c = connection.cursor()

    c.execute("SELECT * FROM room_temp ORDER BY time DESC LIMIT 10")
    res = c.fetchall()
    print("Latest room_temp:")
    for r in res:
        t = datetime.fromtimestamp(r[0])
        print("Time: ", t, " TempC: ", round(r[1], 2), " Acti:", r[2])

    c.execute("SELECT * FROM server_temp ORDER BY time DESC LIMIT 10")
    res = c.fetchall()

    print("Latest server_temp:")
    for r in res:
        t = datetime.fromtimestamp(r[1])
        print("Name: ", r[0], "Time: ", t, " TempC: ", r[2])

    c.execute("SELECT * FROM room_humidity ORDER BY time DESC LIMIT 10")
    res = c.fetchall()

    print("Latest room_humidity:")
    for r in res:
        t = datetime.fromtimestamp(r[1])
        print("Name: ", r[0], "Time: ", t, " Humidity (%): ", r[2])

    c.close()
    connection.close()


if __name__ == "__main__":

    if len(sys.argv) > 1:
        db_path = pathlib.Path(sys.argv[1])
    else:
        db_path = pathlib.Path.home() / ".home_service" / "home_service.db"

    if not db_path.exists():
        raise ValueError("Database file does not exist ({})".format(db_path.as_posix()))

    print_latest_data(db_path.as_posix())
