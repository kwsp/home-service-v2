from .base import db


class Devices(db.Model):
    """
    """

    __tablename__ = "devices"
    device_id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    device_name = db.Column(db.VARCHAR)
    last_active = db.Column(db.DateTime)
