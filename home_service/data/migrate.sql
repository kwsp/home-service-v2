CREATE TABLE server_temp (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name varchar(255) NOT NULL,
    time DATETIME NOT NULL,
    value REAL NOT NULL
);

INSERT INTO server_temp(name, time, value)
SELECT name, datetime(timestamp, 'unixepoch'), temperature FROM pi_temp;

DROP TABLE pi_temp;


CREATE TABLE room_temp (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    time DATETIME NOT NULL,
    value REAL NOT NULL
);

INSERT INTO room_temp (name, time, value)
SELECT name, datetime(timestamp, 'unixepoch'), temperature FROM sensor_temp;

DROP TABLE sensor_temp;


CREATE TABLE room_humidity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    time DATETIME NOT NULL,
    value REAL NOT NULL
);

INSERT INTO room_humidity (name, time, value)
SELECT name, datetime(timestamp, 'unixepoch'), humidity FROM sensor_humidity;
DROP TABLE sensor_humidity
