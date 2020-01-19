from .base import db


class room_temp(db.Model):
    """
    """

    __tablename__ = "room_temp"
    __table_args__ = {"extend_existing": True}
    temp_id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    name = db.Column(db.VARCHAR, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    temperature = db.Column(db.REAL, nullable=False)
