from . import models


class QueryBooks:

    db_path = './database/books'
    binds = {
        name: f'sqlite:///database/books/{name}.sqlite3' for name in [
            "user_register", "blog", "jupyter_app", "music_app"
        ]
    }

    def set_books(self, app, init_db):
        database = dict()
        db = init_db(app=app)
        for name in list(self.binds):
            model = self.get_model(app=app, name=name)
            database[name] = model.__dict__[name]
        return db, database

    @staticmethod
    def get_model(app, name):
        db = __import__("flask_sqlalchemy").__dict__["SQLAlchemy"](app=app)
        model = models.select_model(Model=db.Model, name=name)
        db.__setattr__(name, model)
        db.create_all(bind=[name])
        return db

    @staticmethod
    def check_values(data, conditional=all):
        return True if conditional([
            value is not None for value in data.values()
        ]) else False

    @staticmethod
    def query_filter(book, data):
        if book.repr in list(data):
            return book.query.filter(book.__dict__[book.repr] == data[book.repr]).first()
        elif book.secondary_repr in list(data):
            return book.query.filter(book.__dict__[book.secondary_repr] == data[book.secondary_repr]).first()
        else:
            return None

    @staticmethod
    def query_all(book):
        return book.query.all()

    def get(self, db, book, data):
        if self.check_values(data, conditional=any):
            return {
                book_data.__dict__[book.repr]: {
                    arg: book_data.__dict__[arg] for arg in book.args
                } for book_data in self.query_filter(book, data)
            }
        else:
            return {
                book_data.__dict__[book.repr]: {
                    arg: book_data.__dict__[arg] for arg in book.args
                } for book_data in self.query_all(book)
            }

    def add(self, db, book, data):
        if self.check_values(data):
            data.update({
                book.repr: len(self.query_all(book)) + 1
            })
            db.session.add(book(data=data))
            db.session.commit()
        else:
            return None

    def delete(self, db, book, data):
        if self.check_values(data, conditional=any):
            book_data = self.query_filter(book, data)
            if book_data is None:
                return None
            else:
                db.session.query(book).delete(book_data)
                db.session.commit()
        else:
            return None

    def update(self, db, book, data):
        if self.check_values(data, conditional=any):
            book_data = self.query_filter(book, data)
            if book_data is None:
                return None
            else:
                query_data = {
                    arg: data[arg] if data[arg] is not None else book_data.__dict__[arg] for arg in book.args
                }
                db.session.query(book).update(query_data)
                db.session.commit()
        else:
            return None
