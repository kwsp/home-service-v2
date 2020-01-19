from .base import db


class room_humidity(db.Model):
    """
    """

    __tablename__ = "room_humidity"
    __table_args__ = {"extend_existing": True}
    humidity_id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    name = db.Column(db.VARCHAR, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    humidity = db.Column(db.REAL, nullable=False)
