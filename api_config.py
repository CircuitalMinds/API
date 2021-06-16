import yaml


def imports(app_mode):
    options = lambda name: {
        "flask": ['Flask', 'jsonify', 'request', 'send_file', 'render_template'],
        "flask_restful": ["Resource", "Api"],
        "flask_sqlalchemy": ["SQLAlchemy"],
        "flask_cors": ["CORS"],
        "flask_login": ["LoginManager"],
        "flask_socketio": ["SocketIO"]
    }[name]
    return dict(
        app=dict(flask=options('flask')),
        api=dict(
            flask=options('flask'),
            flask_restful=options('flask_restful'),
            flask_sqlalchemy=options('flask_sqlalchemy'),
            flask_cors=options('flask_cors'),
            flask_login=options('flask_login'),
            flask_socketio=options('flask_socketio'))
    )[app_mode]


class CircuitalMinds:
    __name__ = 'circuitalminds_api'
    models = dict(user_register=object,
                  blog=object,
                  jupyter_app=object,
                  music_app=object)

    def __init__(self):
        self.settings = yaml.load(open('./_config.yml'), Loader=yaml.FullLoader)

    def get_server(self, mode):
        server = dict()
        modules = self.get_object(data=self.set_imports(**imports(app_mode=mode)))
        server.update(dict(settings=self.settings[mode], modules=modules))
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
    def set_imports(**data):
        import_data = {}
        for lib in data.keys():
            import_lib = __import__(lib)
            for module in data[lib]:
                import_data[module] = import_lib.__dict__[module]
        return import_data

