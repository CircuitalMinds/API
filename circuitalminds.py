from api_config import CircuitalMinds
from database import query_books

circuitalminds = CircuitalMinds()
server = circuitalminds.get_server()
api_modules = server.modules
settings = server.settings
app = server.app
api = api_modules.Api(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_BINDS'] = query_books.binds

database = query_books.model_names
query_books.set_books(app=app, init_db=api_modules.SQLAlchemy)
api_modules.CORS(app=app)
login = api_modules.LoginManager(app=app)
session = app.session_interface
socket = api_modules.SocketIO(app, manage_session=False)


class API(api_modules.Resource):

    def __init__(self):
        self.request = api_modules.request
        self.options = {"add": lambda query: self.get_data_to_add(query=query),
                        "delete": lambda query: self.get_data_to_delete(query=query),
                        "update": lambda query: self.get_data_to_update(query=query),
                        "get": lambda query: self.get_data_by_query(query=query)
                        }
        self.select_option = lambda option, query: self.options[option](query=query)

    def get_request_function(self):
        if self.request.method == "POST":
            return lambda argument: self.request.form[argument]
        else:
            return lambda argument: self.request.args.get(argument)

    def get(self, query, option):
        check_query, check_option = query in list(database.keys()), option in list(self.options.keys())
        if all([check_query, check_option]):
            return api_modules.jsonify(self.select_option(option=option, query=query))
        else:
            causes = []
            if check_query is False:
                causes.append(f" [register with {query} not found in database] ")
            if check_option is False:
                causes.append(f" [option {option} not found] ")
            return api_modules.jsonify({"Response": "".join(causes)})


api.add_resource(API, "/get/<query>/<option>")

if __name__ == '__main__':
    socket.run(app, **settings)
