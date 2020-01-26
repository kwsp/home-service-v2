from .base import db, Mixin


class RoomTemp(Mixin, db.Model):
    """
    """

    __tablename__ = "room_temp"
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    name = db.Column(db.VARCHAR, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    value = db.Column(db.REAL, nullable=False)
