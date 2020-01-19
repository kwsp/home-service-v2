CREATE TABLE server_temp (
    server_temp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_name varchar(255) NOT NULL,
    time DATETIME NOT NULL,
    temperature REAL NOT NULL
);

INSERT INTO server_temp(device_name, time, temperature)
SELECT name, datetime(timestamp, 'unixepoch'), temperature FROM pi_temp;

DROP TABLE pi_temp;


CREATE TABLE room_temp (
    temp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    time DATETIME NOT NULL,
    temperature REAL NOT NULL
);

INSERT INTO room_temp (name, time, temperature)
SELECT name, datetime(timestamp, 'unixepoch'), temperature FROM sensor_temp;

DROP TABLE sensor_temp;


CREATE TABLE room_humidity (
    humidity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    time DATETIME NOT NULL,
    humidity REAL NOT NULL
);

INSERT INTO room_humidity (name, time, humidity)
SELECT name, datetime(timestamp, 'unixepoch'), humidity FROM sensor_humidity;
DROP TABLE sensor_humidity
