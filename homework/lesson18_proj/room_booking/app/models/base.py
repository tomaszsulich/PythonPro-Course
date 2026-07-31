from ..db import db


class Base(db.Model):
    __abstract__ = True

    def to_dict(self, exclude=None):
        exclude = exclude or set()

        data = {}
        for col in self.__table__.columns:
            if col.name not in exclude:
                data[col.name] = getattr(self, col.name)
        return data
