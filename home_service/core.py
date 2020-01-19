"""
Utility stuff
"""
import json
import configparser
import logging
from typing import Tuple

from flask import jsonify
from flask.wrappers import Response


class Mixin:
    """Base class for SQLAlchemy Models
    """

    def to_dict(self) -> dict:
        """Method to serialise SQLAlchemy response for JSON

        :returns <dict>
        """
        d_out = dict((key, val) for key, val in self.__dict__.items())
        d_out.pop("_sa_instance_state", None)
        d_out["_id"] = d_out.pop("id", None)  # rename id key to interface with response
        return d_out


def create_response(
    data: dict = None, status: int = 200, message: str = ""
) -> Tuple[Response, int]:
    """Wrapper function to make API responses consistent :)

    Data must be a dictionary
        key: type of data
        value: data
    
    :param data <dict> optional data
    :param status <int> optional status code (defaults to 200)
    :param message <str> optional message
    :returns tuple (<Flask Response>, <int>)
    """

    if type(data) is not dict and data is not None:
        raise TypeError("data must be a dictionary!")

    response = {"success": 200 <= status < 300, "message": message, "result": data}
    return jsonify(response), status


def exception_handler(error: Exception) -> Tuple[Response, int]:
    """Catch all exceptions
    :param Exception
    :returns Tuple(<Flask Response>, <int>)
    """
    return create_response(message=str(error), status=500)


def get_database_url(file: str = "credentials.config") -> str:
    """Load config
    Example of config file:
    [mysql_creds]
    mysql_url = mysql+pymysql://test_user:password@127.0.0.1:3306/ssd_sample_database

    :param file <str> filename
    :returns str or None if Exception
    """
    try:
        config = configparser.ConfigParser()
        config.read(file)
        try:
            res = config["mysql_credentials"]
            return res["mysql_url"]
        except KeyError:
            print("Failed to retrieve MySQL credentials from [{}].".format(file))
    except:
        print("Failed to load config file [{}].".format(file))

