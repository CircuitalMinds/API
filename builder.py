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


def deployment_files():
    requirements = """
    flask
    flask-cors
    flask_sqlalchemy
    gunicorn
    PyYAML
    requests
    Werkzeug
    """
    files = {
        "runtime.txt": "python-3.9.7",
        "Procfile": "web: gunicorn app:app",
        "requirements.txt": requirements
    }
    return files


def installer():
    files = {
        "requirements.txt": deployment_files()["requirements.txt"],
        "install.sh": "\n".join([
            "#!/bin/bash",
            " && ".join([
                "pip install virtualenv",
                "python -m virtualenv environment",
                "source ./environment/bin/activate",
                "pip install -r requirements.txt"
            ])
        ])
    }
    return files


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


def run(app):
    app.run(**settings["server"])
    return
