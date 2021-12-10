from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime


def select_model(db, name):
    Model = db.Model

    class Users(Model):
        id = Column(Integer, primary_key=True, unique=True)
        username = Column(String(50), nullable=False, unique=True)
        password = Column(String(50), nullable=False)
        __bind_key__ = 'users'
        args = {
            "all": ["username", "password"],
            "get": {"required": ["username", "password"], "optional": []},
            "add": {"required": ["username", "password"], "optional": []},
            "update": {"required": ["username", "password", "new_password"], "optional": []},
            "delete": {"required": ["username", "password"], "optional": []}
        }
        repr = "id"

        def __init__(self, data):
            for k, v in data.items():
                self.__setattr__(k, v)

        @classmethod
        def set_data(cls, data, method):
            x = {}
            for key in cls.args[method]["required"]:
                if key in data:
                    x[key] = data[key]
                else:
                    return {}
            for key in cls.args[method]["optional"]:
                if key in data:
                    x[key] = data[key]
            return x

        def __repr__(self):
            return '<Users %r>' % self.id

    class Videos(Model):
        id = Column(Integer, primary_key=True, unique=True)
        title = Column(String(50), nullable=False, unique=True)
        url = Column(String(50), nullable=False)
        image = Column(String(50), nullable=False)
        __bind_key__ = 'videos'
        args = {
            "all": ["title", "url", "image"],
            "get": {"required": [], "optional": ["title", "url", "image"]},
            "add": {"required": ["title", "url", "image"], "optional": []},
            "update": {"required": ["title"], "optional": ["url", "image"]},
            "delete": {"required": ["title"], "optional": ["url", "image"]},
        }
        repr = "id"

        def __init__(self, data):
            for k, v in data.items():
                self.__setattr__(k, v)

        @classmethod
        def set_data(cls, data, method):
            x = {}
            for key in cls.args[method]["required"]:
                if key in data:
                    x[key] = data[key]
                else:
                    return {}
            for key in cls.args[method]["optional"]:
                if key in data:
                    x[key] = data[key]
            return x

        def __repr__(self):
            return '<Videos %r>' % self.id

    class Posts(Model):
        id = Column(Integer, primary_key=True, unique=True)
        title = Column(String(50), nullable=False, unique=True)
        tags = Column(String(50), nullable=False)
        url = Column(String(50), nullable=False)
        image = Column(String(50), nullable=False)
        date = Column(DateTime, default=datetime.utcnow)
        __bind_key__ = 'posts'
        args = {
            "all": ["title", "tags", "url", "image"],
            "get": {"required": [], "optional": ["title", "tags", "url", "image"]},
            "add": {"required": ["title", "tags", "url", "image"], "optional": []},
            "update": {"required": ["title"], "optional": ["tags", "url", "image"]},
            "delete": {"required": ["title"], "optional": ["tags", "url", "image"]},
        }
        repr = "id"

        def __init__(self, data):
            for k, v in data.items():
                self.__setattr__(k, v)

        @classmethod
        def set_data(cls, data, method):
            x = {}
            for key in cls.args[method]["required"]:
                if key in data:
                    x[key] = data[key]
                else:
                    return {}
            for key in cls.args[method]["optional"]:
                if key in data:
                    x[key] = data[key]
            return x

        def __repr__(self):
            return '<Posts %r>' % self.id
    model = {"users": Users, "videos": Videos, "posts": Posts}.get(name)
    db.create_all(bind=[name])
    return model
