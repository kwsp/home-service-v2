import time
import sqlite3
from flask import Flask, jsonify
from flask import make_response, render_template
from flask_restful import Resource, Api, reqparse
from werkzeug.middleware.proxy_fix import ProxyFix

from get_db import get_db, execute_db, init_app

parser = reqparse.RequestParser()
parser.add_argument('n', type=int, help="ERROR: empty length of data")


class SensorData(Resource):
    def get(self):
        return {"test": "test"}
        breakpoint()
        data = parser.parse_args()
        n_points = data.get('n')
        if n_points is None:
            n_points = 1000

        try:
            with get_db() as connection:
                cursor = connection.cursor()
                cursor.execute('''
                SELECT timestamp, temperature, activity FROM sensor_data
                ORDER BY timestamp DESC LIMIT {}'''.format(n_points))
                data = cursor.fetchall()
                timestamp = [tup[0] for tup in data]
                temperature = [tup[1] for tup in data]
                activity = [tup[2] for tup in data]
                cursor.close()
        except sqlite3.OperationalError:
            return {"error": "Querry failed"}

        return {'timestamp': timestamp,
                'temperature': temperature,
                'activity': activity}


class PiTemp(Resource):
    def get(self):
        data = parser.parse_args()
        n_points = data.get('n')
        if n_points is None:
            n_points = 1000

        try:
            with get_db() as connection:
                cursor = connection.cursor()
                cursor.execute('''
                SELECT name, timestamp, temperature FROM pi_temp
                ORDER BY timestamp DESC LIMIT {}'''.format(n_points))
                data = cursor.fetchall()
                cursor.close()
        except sqlite3.OperationalError:
            return {"error": "Querry failed"}

        names = set(v[0] for v in data)
        res = {}
        for name in names:
            timestamp = [v[1] for v in data if v[0] == name]
            temperature = [v[2] for v in data if v[0] == name]
            res[name] = {'timestamp': timestamp, 'temperature': temperature}
        return res

    def post(self):
        parser.add_argument('name', type=str)
        parser.add_argument('temperature', type=float)
        args = parser.parse_args()
        name = args["name"]
        temperature = args["temperature"]
        timestamp = int(time.time())

        if name is None or temperature is None:
            return {"error": "Missing arguments"}

        try:
            with get_db() as connection:
                cursor = connection.cursor()
                cursor.execute('''
                INSERT INTO pi_temp
                VALUES (?,?,?)''', (name, timestamp, temperature))
                cursor.close()
        except sqlite3.OperationalError:
            return {"error": "Querry failed"}

        return {
            'status': True,
            'name': args['name'],
            'temperature': args['temperature']
        }


def create_app():

    # Instantiate flask app
    app = Flask(__name__, instance_relative_config=True)
    init_app(app)

    # Proxy support for NGINX
    app.wsgi_app = ProxyFix(app.wsgi_app)

    # Configure to see multiple erros in response
    app.config['BUNDLE_ERRORS'] = True

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': "Not found"}), 404)

    # Flask_restful API
    api = Api(app)
    api.add_resource(SensorData, '/home_api/get_curr_data')
    api.add_resource(PiTemp, '/home_api/pi_temp')
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(port="8777", debug=True)
