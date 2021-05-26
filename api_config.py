import yaml


class CircuitalMinds:
    __name__ = 'circuitalminds_api'
    api_imports = {
        "flask_sqlalchemy": ["SQLAlchemy"],
        "flask_restful": ["Resource", "Api"],
        "flask": ['Flask', 'jsonify', 'request', 'send_file']
    }
    models = dict(user_register=object,
                  blog=object,
                  jupyter_app=object,
                  music_app=object)

    def __init__(self):
        self.settings = yaml.load(open('./_config.yml'), Loader=yaml.FullLoader)

    def get_server(self):
        server = dict()
        modules = self.get_object(data=self.get_import(**self.api_imports))
        server.update(dict(settings=self.settings['api'], modules=modules))
        init_app = modules.Flask
        app = init_app(__name__)
        app.name = self.__name__
        app.config.update(self.settings['environment'])
        server.update(dict(app=app))
        return self.get_object(server)

    @staticmethod
    def get_model(app, name):
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///database/{name}.sqlite3'
        db = __import__("flask_sqlalchemy").__dict__["SQLAlchemy"](app=app)
        model = __import__("models").select_model(Model=db.Model, name=name)
        db.__setattr__(name, model)
        db.create_all()
        return model

    @staticmethod
    def get_object(data):
        items = data.items()
        obj = __class__()
        for key, value in items:
            obj.__setattr__(key, value)
        return obj

    @staticmethod
    def get_import(**data):
        imports = {}
        for lib in data.keys():
            import_lib = __import__(lib)
            for module in data[lib]:
                imports[module] = import_lib.__dict__[module]
        return imports

    @staticmethod
    def run_api():
        import sys
        options = {}
        for arg in sys.argv[1:]:
            key, value = arg.split("=")
            options[key] = value
