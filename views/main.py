from flask import Blueprint, jsonify, request
main = Blueprint("main", __name__)


@main.route("/")
def home():
    return jsonify(response="main-route")


@main.route("/send-json/", methods=["GET", "POST"],)
def json_view():
    headers = request.headers
    if headers.get("Content-Type") == "application/json":
        return request.json
    else:
        datajson = dict()
        for q in request.query_string.decode("utf-8").split("&"):
            t = q.split("=")
            if len(t) == 2:
                datajson[t[0]] = t[-1]
        return jsonify(datajson)
