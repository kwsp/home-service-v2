from .base import db


class server_temp(db.Model):
    """
    """

    __tablename__ = "server_temp"
    __table_args__ = {"extend_existing": True}
    server_temp_id = db.Colmn(db.INTEGER, primary_key=True, nullable=False)
    device_name = db.Column(db.VARCHAT, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    temperature = db.Column(db.REAL, nullable=False)
