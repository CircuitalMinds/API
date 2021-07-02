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


@app.route('/', methods=['GET', 'POST'])
def info():
    from python_resources import utils
    return utils.open_object_file(path='./python_resources/info.json')


@app.route('/test', methods=['GET', 'POST'])
def test_register():
    from python_resources import utils
    queries = utils.open_object_file(path='./info_db.json')['database']
    books = [{"name": q, "args": queries[q]['arguments']} for q in queries.keys()]
    return api_modules.render_template('register.html', books=books)

def grapher(args):
    import base64
    from io import BytesIO
    import numpy as np
    from matplotlib.figure import Figure
    a, b, n = int(args["a"]), int(args["b"]), int(args["n"])
    x = np.linspace(a, b, n)
    y = {"cos": np.cos, "sin": np.sin}[args["function"]](x)
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot(x, y)
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"

import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig


if __name__ == '__main__':
    socket.run(app, **settings)
