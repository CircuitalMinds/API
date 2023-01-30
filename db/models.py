from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


'''
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime


class Model:
    types = dict(
        int=dict(value=Integer, opts=dict(primary_key=True, unique=True)),
        name=dict(value=String(100), opts=dict(nullable=False, unique=True)),
        text=dict(value=String(100), opts=dict(nullable=False)),
        date=dict(value=DateTime, opts=dict(default=datetime.utcnow))
    )

    def __init__(self, **attrs):
        self.id = self.col("int")
        for name, attr in attrs.items():
            xtype = attr["datatype"]
            xdata = attr["opts"] if "opts" in attr else {}
            setattr(self, name, self.col(xtype, **xdata))
        def query_all():
            return {
                i.id: {
                    arg: getattr(i, arg) for arg in self.args
                } for i in self.query.all()
            }

        def query_filter(data_id, first=True):
            q = self.query.filter_by(self.id == data_id)
            if first:
                return q.first()
            else:
                return q

        def add(**data):
            self.set_data(**data)
            db.session.add(self)
            db.session.commit()
            return {"message": "data added successfully"}

        def update(old_data, new_data):
            q = self.query_filter(old_data['id'])
            q.__dict__.update(new_data)
            db.session.query(self).update(q)
            db.session.commit()

        def delete(data):
            q = self.query_filter(data['id'])
            db.session.query(self).delete(q)
            db.session.commit()

        super().__init__(**attrs)


    def col(self, datatype, **data):
        typed, opts = (self.types[datatype][i] for i in ("value", "opts"))
        opts.update(data)
        return Column(typed, **opts)


def getbook(db):

    class User(Model, db.Model):
        dict(
            username=dict(datatype="name"),
            email=dict(datatype="text"),
            password=dict(datatype="text")
        )
        __bind_key__ = "user"

        def set_data(self, **data):
            for arg in self.args:
                setattr(self, arg, data[arg])

        def __repr__(self):
            return '<User %r>' % self.id

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
    db.create_all(bind=[name])
    return table
'''

