from flask import Blueprint, jsonify
from os import kill, getpid
from signal import SIGINT
admin = Blueprint("admin", __name__)


@admin.route("/admin/")
def admin_root():
    return jsonify(response="admin-route")


@admin.route("/admin/")
@admin.route("/admin/shutdown/")
def admin_shutdown():
    kill(getpid(), SIGINT)
    return jsonify(
        success=True,
        message="Server is shutting down..."
    )
