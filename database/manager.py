from . import models, query_tools
from os import listdir


class QueryBooks:
    model_names = [name.replace('.sqlite3', '') for name in listdir('./database/books')]
    binds = {name: f'sqlite:///database/books/{name}.sqlite3' for name in model_names}
    handlers = query_tools

    def set_books(self, app, init_db):
        database = dict()
        db = init_db(app=app)
        for name in self.model_names:
            model = self.get_model(app=app, name=name)
            database[name] = model.__dict__[name]
            db.__setattr__(name, model.__dict__[name])

    def get_model_names(self):
        import os
        books_path = './database/books'
        for name in os.listdir(books_path):
            if name.endswith('sqlite3'):
                name = name.replace('.sqlite3', '')
                self.model_names.append(name)

    @staticmethod
    def get_model(app, name):
        db = __import__("flask_sqlalchemy").__dict__["SQLAlchemy"](app=app)
        model = models.select_model(Model=db.Model, name=name)
        db.__setattr__(name, model)
        db.create_all(bind=[name])
        return db

    def get_data_to_add(self, book, args):
        data = {}
        arguments = book.args
        for arg in args:
            if arg is None:
                return {"Response": f"{arg} not found in request"}
            else:
                data[arg] = arg

    def get_data_to_delete(self, book, reprs):
        data = {}
        repr = book.repr
        secondary_repr = book.secondary_repr
        for to_repr in [repr, secondary_repr]:
            repr_data = reprs
            if repr_data is not None:
                data[to_repr] = repr_data
        if data == {}:
            return {"Response": f"data to {repr} or {secondary_repr} not found in request"}
        else:
            return

    def get_data_to_update(self, book):
        with_repr = {}
        argument_update = {}
        secondary_repr = book.secondary_repr
        for to_repr in [repr, secondary_repr]:
            repr_data = book.repr
            if repr_data is not None:
                with_repr[to_repr] = repr_data
                break
        if with_repr == {}:
            return {"Response": f"data to {repr} or {secondary_repr} not found in request"}
        for argument in book.args:
            if all([argument != repr, argument != secondary_repr]):
                argument_data = book.args
                if argument_data is not None:
                    argument_update[argument] = argument_data
        if argument_update == {}:
            return {"Response": f"data to update not found in request"}
        else:
            print(with_repr, argument_update)

    def get_data_by_query(self, book):
        data = {}
        repr = book.repr
        secondary_repr = book.secondary_repr
        for repr_data in [repr, secondary_repr]:
            if repr_data is not None:
                data[repr_data] = repr_data
                break
        if data == {}:
            return
        else:
            return
