from .base import db, Mixin


class RoomHumidity(Mixin, db.Model):
    """
    """

    __tablename__ = "room_humidity"
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    name = db.Column(db.VARCHAR, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    value = db.Column(db.REAL, nullable=False)

    def __repr__(self):  # pragma: no cover
        return "<RoomHumidity {!r}, {!r}, {!r}>".format(
            self.name, self.time, self.value
        )
