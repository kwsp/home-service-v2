import os


class Config:
    """Base config
    """

    SECRET_KEY = "myprecious"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_FILE = "api.log"


class DevelopmentConfig(Config):
    """Dev config
    """

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///data/tiger-home.db"


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///data/tiger-home.db"
