from builder import init_app, init_db
from database.handlers import get_data, add_data, update_data, delete_data, request_handler
from flask import jsonify, send_file, request, redirect, url_for
from drive import Storage, join
app = init_app()
db = init_db(app)
storage = Storage()


@app.route("/", methods=["GET"])
def home():
    host = "https://circuitalminds.github.io"
    page = "drive"
    return redirect(join(host, page))


@app.route("/api/<query>/", methods=["GET"])
@app.route("/api/<query>/<method>/", methods=["GET", "POST"])
def api_query(query="", method=""):
    handler = {
        f.__name__.split("_")[0]: f
        for f in (get_data, add_data, update_data, delete_data)
    }
    if query in db.books and method in handler:
        return jsonify(handler[method](db, query))
    else:
        return jsonify({"response": "data invalid"})


@app.route("/api/drive/", methods=["GET"])
@app.route("/api/drive/<method>", methods=["GET", "POST"])
def api_storage(method=""):
    data = request_handler()
    if method == "get" and "filename" in data:
        file_data = storage.get(data["filename"])
        if all([key in file_data for key in ("filename", "path")]):
            return send_file(file_data["path"], download_name=file_data["filename"])
        else:
            return jsonify(file_data)
    elif method == "upload":
        files = request.files.getlist("files[]")
        for fi in files:
            storage.upload(fi)
        return redirect(url_for("home"))
    else:
        return jsonify({"response": f"method {method} not allowed"})
