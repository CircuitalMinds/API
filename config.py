from flask import Flask, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from json import load
from db import get_table
from flask import jsonify, request


def load_data():
    data = load(open("settings.json"))
    db_data, env, folders, server = (data[i] for i in ("db", "env", "folders", "server"))
    uri, ext, tables = (db_data[i] for i in ("uri", "ext", "tables"))
    env["SQLALCHEMY_BINDS"].update({i: f"{uri}/{i}.{ext}" for i in tables})
    return dict(env=env, folders=folders, server=server)


class Cfg:
    data = load_data()

    @staticmethod
    def get(key):
        return Cfg.data.get(key)


def create_app():
    app = Flask("app", **Cfg.get("folders"))
    app.config.update(Cfg.get("env"))
    CORS(app)
    return app


def create_db(app):
    db = SQLAlchemy(app)
    for name in Cfg.get("env")["SQLALCHEMY_BINDS"]:
        setattr(db, name, get_table(name, SQLAlchemy(app)))
    return db


def get_request():
    query_string = list(filter(
        lambda i: len(i) == 2,
        [s.split("=") for s in request.query_string.decode("utf-8").split("&")]
    ))
    return {x[0]: x[1] for x in query_string}


def add_routes(app, db):

    @app.route("/", methods=["GET", "POST"])
    def home():
        return render_template("index.html")

    @app.route("/", methods=["GET", "POST"])
    @app.route("/user/", methods=["GET", "POST"])
    @app.route("/user/<opt>/", methods=["GET", "POST"])
    def user_route(opt=None):
        data = {}
        if opt == "query_all":
            data.update(db.user.query_all())
        if opt == "add":
            data.update(db.user.add(**get_request()))
        return jsonify(data)

    @app.route("/", methods=["GET", "POST"])
    @app.route("/logger/", methods=["GET", "POST"])
    @app.route("/logger/<opt>/", methods=["GET", "POST"])
    def logger_route(opt=None):
        data = {}
        if opt == "query_all":
            data.update(db.logger.query_all())
        if opt == "add":
            data.update(db.logger.add(**get_request()))
        return jsonify(data)
