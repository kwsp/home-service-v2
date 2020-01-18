from flask import Flask, jsonify
from flask import make_response, render_template
from flask_restful import Api
from werkzeug.middleware.proxy_fix import ProxyFix

from home_service.get_db import init_app

from home_service.endpoints import sensor_blueprint

def create_app():

    # Instantiate flask app
    app = Flask(__name__, instance_relative_config=True)
    init_app(app)

    # Proxy support for NGINX
    app.wsgi_app = ProxyFix(app.wsgi_app)

    # Configure to see multiple errors in response
    app.config['BUNDLE_ERRORS'] = True

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/debug')
    def debug():
        return render_template('debug.html')

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': "Not found"}), 404)

    app.register_blueprint(sensor_blueprint.sensor_blueprint)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(port="6969", debug=True)
