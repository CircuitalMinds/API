from database import query_books
import yaml
config = dict(
    production={"host": "circuitalminds.herokuapp.com", "port": 80, "debug": False},
    deployment={"host": "127.0.0.1", "port": 5000, "debug": True},
    environment={
        "secret_key": "circuitalminds", "session_type": "filesystem",
        'SQLALCHEMY_TRACK_MODIFICATIONS': False, 'SQLALCHEMY_BINDS': query_books.binds
    },
    imports={
        "flask": ['Flask', 'jsonify', 'request', 'send_file', 'render_template', 'redirect', 'url_for'],
        "flask_restful": ["Resource", "Api"],
        "flask_sqlalchemy": ["SQLAlchemy"],
        "flask_cors": ["CORS"],
        "flask_login": ["LoginManager"],
        "flask_socketio": ["SocketIO"]
    }
)


def build_config():
    opt = input(
        "config app as deployment (1) or production (2) mode. (Enter) to pass: "
    )
    if opt == '':
        pass
    else:
        opt = int(opt)
        with open('_config.yml', "w") as outfile:
            yaml.dump(
                config["deployment"] if opt == 1 else config["production"],
                outfile, default_flow_style=False
            )


class CircuitalMinds:
    __name__ = 'circuitalminds'

    def __init__(self):
        self.settings = yaml.load(open('./_config.yml'), Loader=yaml.FullLoader)

    def get_server(self):
        modules = self.get_object(self.set_imports())
        app = self.init_app(self.__name__)
        api = modules.Api(app)
        query_tools = query_books()
        server = {
            "modules": self.get_object(self.set_imports()),
            "app": app, "api": api,
            "set_books": query_tools.set_books,
            "query_tools": {
                "get": query_tools.get,
                "add": query_tools.add,
                "delete": query_tools.delete,
                "update": query_tools.update
            }
        }
        return self.get_object(server)

    @staticmethod
    def init_app(name):
        app = __import__("flask").__dict__["Flask"](__name__)
        app.name = name
        app.config.update(config['environment'])
        return app

    def init_socket(self, app):
        __import__('flask_cors').__dict__["CORS"](app=app)
        login = __import__("flask_login").__dict__["LoginManager"](app=app)
        session = app.session_interface
        socket = __import__("flask_socketio").__dict__["SocketIO"](app, manage_session=False)
        run = lambda: socket.run(app, **self.settings)
        return login, session, socket, run

    @staticmethod
    def get_object(data):
        obj = __class__()
        [obj.__setattr__(key, value) for key, value in data.items()]
        return obj

    @staticmethod
    def set_imports():
        import_data = {}
        for lib, modules in config["imports"].items():
            import_lib = __import__(lib)
            import_data.update({
                module: import_lib.__dict__[module] for module in modules
            })
        return import_data
