from flask import Flask, json
from flask_cors import CORS
from werkzeug.exceptions import HTTPException
from config import conf
from view import add_view
app = Flask(
    __name__,
    static_folder=conf["static_folder"],
    template_folder=conf["template_folder"]
)
app.config.update(conf["app-config"])
CORS(app)


def getresponse(info, **params):
    response = info.get_response()
    response.data = json.dumps(
        params if params else {
            i: getattr(info, i, None)
            for i in ("code", "name", "description")
        }
    )
    response.content_type = "application/json"
    return response


@app.errorhandler(HTTPException)
def handle_exception(error):
    return getresponse(error)


add_view(
    app, "main", "admin", "container"
)

if __name__ == "__main__":
    app.run(**conf["app-server"])
