from database import query_books
from flask import Flask
from flask_restful import Api
config = dict(
    production={"host": "https://circuitalminds.herokuapp.com/", "port": 80, "debug": False},
    development={"host": "192.168.50.7", "port": 5000, "debug": True},
    environment={
        "secret_key": "circuitalminds", "session_type": "filesystem"
    }
)


class CircuitalMinds:
    __name__ = 'circuitalminds'

    def get_server(self):
        app = Flask(self.__name__, template_folder="./templates")
        app.config.update(config['environment'])
        api = Api(app)
        query_tools = query_books()
        server = {
            "app": app, "api": api,
            "set_books": query_tools.set_books,
            "query_tools": {
                "get": query_tools.get,
                "add": query_tools.add,
                "delete": query_tools.delete,
                "update": query_tools.update
            }
        }
        return server

    @staticmethod
    def init_app(name):
        app = __import__("flask").__dict__["Flask"](__name__)
        app.name = name
        app.config.update(config['environment'])
        return app
