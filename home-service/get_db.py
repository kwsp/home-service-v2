import os
import sqlite3

from flask import g
from flask.cli import with_appcontext


# Get DB path
db_name = "tiger-home.db"
db_path = os.path.join(os.getcwd(),
                       '/data',
                       db_name)


def db():
    # Create the DB
    return sqlite3.connect(db_path)


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(db_path)
    return g.db


def execute_db(cmd):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(cmd)
    res = cursor.fetchall()
    cursor.close()
    return res


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_app(app):
    app.teardown_appcontext(close_db)
