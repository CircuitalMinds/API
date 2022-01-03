from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from database import models
from utils import get_json
settings = get_json("./", "settings.json")
books = settings["books"]
set_bind = lambda name: f"sqlite:///database/books/{name}.sqlite3"
settings["environment"].update({
    "SQLALCHEMY_BINDS": {
        name: set_bind(name) for name in books
    }
})


def init_app():
    app = Flask("app")
    CORS(app)
    app.config.update(settings["environment"])
    return app


def init_db(app):
    db = SQLAlchemy(app)
    db.__setattr__("books", books)
    for name in books:
        db.__setattr__(name, models.select_model(SQLAlchemy(app), name))
    return db
