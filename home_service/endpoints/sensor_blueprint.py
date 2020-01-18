import time
import datetime
from flask import jsonify, Blueprint, request

from home_service.get_db import get_db, execute_db


sensor_blueprint = Blueprint("sensor_blueprint", __name__)

def insert_name_temperature(table_name, name, data):
    timestamp = int(time.time())
    if 'humidity' in table_name:
        var = 'humidity'
    else:
        var = 'temperature'
    try:
        with get_db() as connection:
            cursor = connection.cursor()
            cursor.execute('''
            INSERT INTO {}
            VALUES (?,?,?)'''.format(table_name),
                           (name, timestamp, data))
            cursor.close()
    except Exception as e:
        return {"Exception Type": str(type(e)),
                "Args": str(e.args),
                "__str__": str(e.__str__)}, 420
    return {
        'status': True,
        'name': name,
        var: data 
    }


def select_names_npoints(table_name, names, n_points):
    ''' If n_points is None, select data from the last day.
        If names is None, select all.
    '''
    if 'humidity' in table_name:
        var = 'humidity'
    else:
        var = 'temperature'

    cmd = '''SELECT name, timestamp, {} FROM {} '''.format(var, table_name)

    if names is not None:
        nm = "'" + "', '".join(names) + "'"
        cmd += ''' WHERE name in ({})
        '''.format(nm)

    if n_points is None:
        if 'WHERE' in cmd:
            cmd += 'AND'
        else:
            cmd += 'WHERE'
        cmd += ''' timestamp BETWEEN {} AND {}'''.format(
                int((datetime.datetime.now()-datetime.timedelta(days=1)).timestamp()),
                int(datetime.datetime.now().timestamp()))
        n_points = 2000

    cmd += ''' ORDER BY timestamp DESC LIMIT {} '''.format(n_points)
    try:
        data = execute_db(cmd)
    except Exception as e:
        return {"Exception Type": str(type(e)),
                "Args": str(e.args),
                "__str__": str(e.__str__)}

    names = set(v[0] for v in data)
    res = {}
    for name in names:
        res[name] = []
    for v in data:
        res[v[0]].append({
            'x': v[1],
            'y': v[2]
        })
    return res


@sensor_blueprint.route("/home_api/sensor_temp", methods=["GET"])
def sensor_temp_get():
    n_points = request.args["n"]
    name = request.args["names"]
    return select_names_npoints('sensor_temp', names, n_points)

@sensor_blueprint.route("/home_api/sensor_temp", methods=["POST"])
def sensor_temp_post():
    name = request.args["names"]
    temperature = request.args["temperature"]

    if name is None or temperature is None:
        return {"error": "Missing arguments"}, 420

    return insert_name_temperature('sensor_temp', name, temperature)

@sensor_blueprint.route("/home_api/sensor_humidity", methods=["GET"])
def sensor_humidity_get():
    name = request.args["names"]
    n_points = request.args["n"]
    return select_names_npoints('sensor_humidity', names, n_points)

@sensor_blueprint.route("/home_api/sensor_humidity", methods=["POST"])
def sensor_humidity_post():
    name = request.args["names"]
    humidity = request.args["humidity"]

    if name is None or humidity is None:
        return {"error": "Missing arguments"}, 420

    return insert_name_temperature('sensor_humidity', name, humidity)


@sensor_blueprint.route("/home_api/pi_temp", methods=["GET"])
def pi_temp_get():
    if not "names" in request.args:
        return {"error": "Missing arguments"}, 420

    if not "n" in request.args:
        return {"error": "Missing arguments"}, 420

    name = request.args["names"]
    n_points = request.args["n"]

    return select_names_npoints('pi_temp', names, n_points)

@sensor_blueprint.route("/home_api/pi_temp", methods=["POST"])
def pi_temp_post():
    if not "names" in request.args:
        return {"error": "Missing arguments"}, 420

    if not "temperature" in request.args:
        return {"error": "Missing arguments"}, 420

    name = request.args["names"]
    temperature = request.args["temperature"]
    timestamp = int(time.time())

    return insert_name_temperature('pi_temp', name, temperature)


# @sensor_blueprint.route("/home_api/gitpull", methods=["GET"])
# def get(repo_name):
    # if repo_name == "tigernie_website":
        # res = os.popen("cd /var/www/tigernie-website && git pull").readline().strip()
        # return jsonify({"status": res})

