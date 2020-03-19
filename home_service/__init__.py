import os

from flask import Flask, jsonify
from flask import make_response, render_template
from werkzeug.middleware.proxy_fix import ProxyFix

from home_service.config import DevelopmentConfig, ProductionConfig, TestingConfig
from home_service.core import exception_handler, create_response
from home_service.models.base import db, init_test_db
from home_service.endpoints import sensor_blueprint


def create_app(testing=False):

    # Instantiate flask app
    app = Flask(__name__)

    # Set config
    env = os.environ.get("FLASK_ENV", "development")

    if testing:
        app.config.from_object(TestingConfig())
    else:
        if env == "development":
            app.config.from_object(DevelopmentConfig())
        elif env == "production":  # pragma no cover
            app.config.from_object(ProductionConfig())

    # Register Database
    db.init_app(app)

    # Initialise Database
    with app.app_context():
        if testing:
            init_test_db()
        else:
            db.create_all()

    # Proxy support for NGINX
    app.wsgi_app = ProxyFix(app.wsgi_app)

    # Dashboard page
    @app.route("/")
    def index():
        return render_template("index.html")

    # Register blueprints
    app.register_blueprint(sensor_blueprint.sensor_blueprint)

    # Register error handler
    if not testing:
        app.register_error_handler(Exception, exception_handler)

    return app
