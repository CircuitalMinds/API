from builder import init_app, init_db, run
from database.handlers import get_data, add_data, update_data, delete_data, request_handler
from flask import jsonify, request, render_template
from drive import Storage
storage = Storage()
app = init_app()
db = init_db(app)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/api/users/", methods=["GET"])
@app.route("/api/users/<option>/", methods=["GET", "POST"])
def api_users(option=None):
    opt = {"get": get_data, "add": add_data, "update": update_data, "delete": delete_data}.get(option)
    if opt:
        return jsonify(opt(db, "users"))
    else:
        return jsonify({"response": "data invalid"})


@app.route("/api/drive/", methods=["GET", "POST"])
def api_drive():
    return storage.route(
        request.method, request_handler()
    )


if __name__ == "__main__":
    run(app)
