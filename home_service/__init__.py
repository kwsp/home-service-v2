import os

from flask import Flask, jsonify
from flask import make_response, render_template
from werkzeug.middleware.proxy_fix import ProxyFix

from home_service.config import DevelopmentConfig, ProductionConfig, TestingConfig
from home_service.core import exception_handler, create_response
from home_service.models.base import db
from home_service.endpoints import sensor_blueprint


def create_app():

    # Instantiate flask app
    app = Flask(__name__)

    # Set config
    env = os.environ.get("FLASK_ENV", "production")

    if env == "development":
        app.config.from_object(DevelopmentConfig)
    elif env == "production":
        app.config.from_object(ProductionConfig)
    elif env == "testing":
        app.config.from_object(TestingConfig)

    # Register Database
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Proxy support for NGINX
    app.wsgi_app = ProxyFix(app.wsgi_app)

    @app.route("/")
    def index():
        return render_template("index.html")

    if env == "development":

        @app.route("/debug")
        def debug():
            return render_template("debug.html")

    app.register_blueprint(sensor_blueprint.sensor_blueprint)
    app.register_error_handler(Exception, exception_handler)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(port="6969", debug=True)
