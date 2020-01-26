from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Mixin:
    """Base class for sensor value tables
    """

    def __repr__(self):
        return "<{!r}: {!r}, {!r}, {!r}>".format(
            self.__tablename__, self.name, self.time, self.value
        )

    def to_dict(self) -> dict:
        """Method to serialise SQLAlchemy response for JSON

        :returns <dict>
        """
        d_out = dict((key, val) for key, val in self.__dict__.items())
        d_out.pop("_sa_instance_state", None)
        d_out["_id"] = d_out.pop("id", None)  # rename id key to interface with response
        return d_out
