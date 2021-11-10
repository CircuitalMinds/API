from flask import request, jsonify, render_template
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from api_config import CircuitalMinds, config
circuitalminds = CircuitalMinds()
server = circuitalminds.get_server()
app, api, query_tools, set_books = [server[i] for i in ("app", "api", "query_tools", "set_books")]
CORS(app)
db, books = set_books(app=app, init_db=SQLAlchemy)


class API(Resource):

    def __init__(self):
        self.data = {}

    @staticmethod
    def query_response(query, option):
        if query in list(books) and option in list(query_tools):
            [book, query_function] = books[query], query_tools[option]
            args = book.args
            args.extend([book.repr, book.secondary_repr])
            get_request = request.form if request.method == "POST" else request.args.get
            request_data = {arg: get_request(arg) for arg in args}
            return query_function(db=db, book=book, data=request_data)
        else:
            return None

    def get(self, query='all'):
        if query == "all":
            return jsonify({
                name: [{
                    arg: q.__dict__[arg] for arg in q.args
                } for q in db.session.query(book).all()] for name, book in books.items()
            })
        else:
            return jsonify({
                query: [{
                    arg: q.__dict__[arg] for arg in q.args
                } for q in db.session.query(books[query]).all() if query in list(books)]
            })


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template(f"github.html")


api.add_resource(API, "/get/<query>")

if __name__ == '__main__':
    app.run()
