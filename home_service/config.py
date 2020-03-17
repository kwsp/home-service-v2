from base64 import b64encode
import os
import configparser


def get_database_path() -> str:
    """
    Store data in ~/.home_service/home_service.db
    """
    data_dir = os.path.join(os.environ["HOME"], ".home_service")
    try:
        os.makedirs(data_dir)
    except OSError:
        pass
    return os.path.join(data_dir, "home_service.db")


class Config:
    """Base config
    """

    DEBUG = False
    LOG_FILE = "api.log"
    SECRET_KEY = b64encode(os.urandom(16)).decode()

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///data/home_service.db"


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + get_database_path()


class TestingConfig(Config):
    TESTING = True
