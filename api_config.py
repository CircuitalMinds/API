import yaml


def get_imports():
    return {
        "flask": ['Flask', 'jsonify', 'request', 'send_file', 'render_template'],
        "flask_restful": ["Resource", "Api"],
        "flask_sqlalchemy": ["SQLAlchemy"],
        "flask_cors": ["CORS"],
        "flask_login": ["LoginManager"],
        "flask_socketio": ["SocketIO"]
    }


class CircuitalMinds:
    __name__ = 'circuitalminds'

    def __init__(self):
        self.settings = yaml.load(open('./_config.yml'), Loader=yaml.FullLoader)

    def get_server(self):
        server = dict()
        modules = self.get_object(data=self.set_imports())
        server.update(dict(settings=self.settings['app'], modules=modules))
        init_app = modules.Flask
        app = init_app(__name__)
        app.name = self.__name__
        app.config.update(self.settings['environment'])
        server.update(dict(app=app))
        return self.get_object(server)

    @staticmethod
    def get_object(data):
        items = data.items()
        obj = __class__()
        for key, value in items:
            obj.__setattr__(key, value)
        return obj

    @staticmethod
    def set_imports():
        import_data = {}
        data = get_imports()
        for lib in data.keys():
            import_lib = __import__(lib)
            for module in data[lib]:
                import_data[module] = import_lib.__dict__[module]
        return import_data

