from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from database import models
from fmod import Obj
config = Obj("./settings.json")
books = config.get("books")


def init_app():
    app = Flask("app", **config.get("app_folders"))
    data = config.get("environment")
    data["SQLALCHEMY_BINDS"].update({
        name: f"sqlite:///database/books/{name}.sqlite3"
        for name in books
    })
    CORS(app)
    app.config.update(data)
    return app


def init_db(app):
    db = SQLAlchemy(app)
    db.__setattr__("books", books)
    for name in books:
        db.__setattr__(
            name, models.select_model(SQLAlchemy(app), name)
        )
    return db


def run(app):
    return app.run(
        **config.get("server")
    )
