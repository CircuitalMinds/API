from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime


class Col:

    @staticmethod
    def id():
        return Column(Integer, primary_key=True, unique=True)

    @staticmethod
    def name():
        return Column(String(100), nullable=False, unique=True)

    @staticmethod
    def text():
        return Column(String(100), nullable=False)

    @staticmethod
    def date():
        return Column(DateTime, default=datetime.utcnow)


def get_table(name, db):

    class User(db.Model):
        id = Col.id()
        username = Col.name()
        email = Col.text()
        password = Col.text()
        args = ("username", "email", "password")
        __bind_key__ = 'user'

        def set_data(self, **data):
            for arg in self.args:
                setattr(self, arg, data[arg])

        def __repr__(self):
            return '<User %r>' % self.id

    class Logger(db.Model):
        id = Col.id()
        issue = Col.name()
        date = Col.date()
        message = Col.text()
        args = ("issue", "date", "message")
        __bind_key__ = 'logger'

        def set_data(self, **data):
            for arg in ("issue", "message"):
                setattr(self, arg, data[arg])

        def __repr__(self):
            return '<Logger %r>' % self.id

    table = dict(user=User, logger=Logger).get(name)

    def query_all():
        cls = table()
        return {
            i.id: {
                arg: getattr(i, arg) for arg in cls.args
            } for i in cls.query.all()
        }

    def query_filter(data_id, first=True):
        cls = table()
        q = cls.query.filter_by(cls.id == data_id)
        if first:
            return q.first()
        else:
            return q

    def add(**data):
        cls = table()
        cls.set_data(**data)
        db.session.add(cls)
        db.session.commit()
        return {"message": "data added successfully"}

    def update(old_data, new_data):
        cls = table()
        q = cls.query_filter(old_data['id'])
        q.__dict__.update(new_data)
        db.session.query(cls).update(q)
        db.session.commit()

    def delete(data):
        cls = table()
        q = cls.query_filter(data['id'])
        db.session.query(cls).delete(q)
        db.session.commit()
    table.query_all = query_all
    table.query_filter = query_filter
    table.add = add
    table.update = update
    table.delete = delete
    db.create_all(bind=[name])
    return table
