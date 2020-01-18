from .base import db

class sensor_humidity(db.Model):
    """
    """
    __tablename__ = "pi_temp"
    timestamp = db.Column(db.DateTime, nullable=False)
    name = db.Column(db.String, nullable=False)
    humidity = db.Column(db.INT, nullable=False)

