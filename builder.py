from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from database import models
from utils import Dumper
fdata = Dumper.open_json("./settings.json").get
books = fdata("books")


def init_app():
    app = Flask("app", **fdata("app_folders"))
    data = fdata("environment")
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
        **fdata("server")
    )
