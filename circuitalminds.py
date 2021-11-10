from api_config import CircuitalMinds


circuitalminds = CircuitalMinds()
server = circuitalminds.get_server()
modules = server.modules
app, api, query_tools = server.app, server.api, server.query_tools
db, books = server.set_books(app=app, init_db= modules.SQLAlchemy)
login, session, socket, run = circuitalminds.init_socket(app)

request, jsonify, resource = modules.request, modules.jsonify, server.modules.Resource


class API(resource):

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

    def get(self, query, option):
        response_data = self.query_response(query, option)
        if response_data is None:
            return jsonify({"Response": "Bad Request"})
        else:
            return jsonify(response_data)


api.add_resource(API, "/get/<query>/<option>")

@app.route("/", methods=["GET", "POST"])
@app.route("/<route>", methods=["GET", "POST"])
def home(route='github'):
    routes = ['github', 'console_app', 'chat_app', 'inbox_app']
    return modules.render_template(f"{route}.html")


if __name__ == '__main__':
    run()
