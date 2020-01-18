from .base import db

class sensor_temp(db.Model):
    """
    """
    __tablename__ = "sensor_temp"
    timestamp = db.Column(db.DateTime, nullable=False)
    name = db.Column(db.String, nullable=False)
    temperature = db.Column(db.INT, nullable=False)

