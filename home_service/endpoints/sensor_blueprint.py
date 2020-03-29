"""
Sensor data endpoints

Get request:
    Args:
        names: <list> of device names. Defaults to all devices.
        begin: <datetime> begining date. Defaults to one day ago.
        end: <datetime> end date. Defaults to now.

    Returns:
        result: list of objects containing {"device_name", "timestamp", "value"}

Post request:
    Args: (Table inferred from endpoint url)
        name: device name. Must provide.
        value: reading value. Must provide.
"""
import time
import json
import datetime
from flask import jsonify, Blueprint, request
from sqlalchemy import func

from home_service.core import create_response
from home_service.models import db, ServerTemp, RoomTemp, RoomHumidity


sensor_blueprint = Blueprint("sensor_blueprint", __name__)


def _sensor_data_get(Table, args):
    """Helper function to get data from the sensor tables
    """

    qry = Table.query.order_by(Table.time.desc())

    if "names" in args:
        qry = qry.filter(func.lower(Table.name).in_([v.lower() for v in args["names"]]))

    end_date = datetime.datetime.now()
    begin_date = end_date - datetime.timedelta(days=1)

    if "begin" in args:
        begin_date = datetime.datetime.fromtimestamp(float(request.args["begin"]))

    if "end" in args:
        end_date = datetime.datetime.fromtimestamp(float(request.args["end"]))

    qry = qry.filter(begin_date < Table.time).filter(Table.time < end_date)
    res = [v.to_dict() for v in qry.all()]

    return create_response(data=res)


def _sensor_data_post(Table, args):
    """Helper function to add data to the sensor tables
    """
    if not args or "name" not in args or "value" not in args:
        return create_response(message="Missing arguments", status=420)

    name = args["name"]
    value = round(args["value"], 2)  # round to 2 decimal places

    if "humidity" in Table.__tablename__ and (value > 100 or value < 0):
        return create_response(
            message="Invalid humidity: cannot exceed 100%", status=420
        )

    new_data_pt = Table(name=args["name"], time=datetime.datetime.now(), value=value)
    db.session.add(new_data_pt)
    db.session.commit()
    return create_response(message="Successfully posted")


@sensor_blueprint.route("/home_api/room_temp", methods=["GET"])
def RoomTemp_get():
    return _sensor_data_get(RoomTemp, request.args)


@sensor_blueprint.route("/home_api/room_temp", methods=["POST"])
def RoomTemp_post():
    return _sensor_data_post(RoomTemp, request.json)


@sensor_blueprint.route("/home_api/room_humidity", methods=["GET"])
def RoomHumidity_get():
    return _sensor_data_get(RoomHumidity, request.args)


@sensor_blueprint.route("/home_api/room_humidity", methods=["POST"])
def RoomHumidity_post():
    return _sensor_data_post(RoomHumidity, request.json)


@sensor_blueprint.route("/home_api/server_temp", methods=["GET"])
def ServerTemp_get():
    return _sensor_data_get(ServerTemp, request.args)


@sensor_blueprint.route("/home_api/server_temp", methods=["POST"])
def ServerTemp_post():
    return _sensor_data_post(ServerTemp, request.json)
