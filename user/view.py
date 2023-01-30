from functools import wraps
from flask import (
    render_template,
    request,
    session,
    flash,
    redirect,
    url_for,
    abort,
    jsonify,
)
from flask_sqlalchemy import SQLAlchemy


# create and initialize a new Flask app
from app import app
# load the config
# init sqlalchemy
db = SQLAlchemy(app)
from . import models


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("logged_in"):
            flash("Please log in.")
            return jsonify({"status": 0, "message": "Please log in."}), 401
        return f(*args, **kwargs)

    return decorated_function


@app.route("/user/")
def user_root():
    """Searches the database for entries, then displays them."""
    entries = db.session.query(models.Post)
    print(entries)
    return render_template("user/index.html", entries=entries)


@app.route("/user/add/", methods=["POST"])
def add_entry():
    """Adds new post to the database."""
    if not session.get("logged_in"):
        abort(401)
    new_entry = models.Post(request.form["title"], request.form["text"])
    db.session.add(new_entry)
    db.session.commit()
    flash("New entry was successfully posted")
    return redirect(url_for("user_root"))


@app.route("/user/login/", methods=["GET", "POST"])
def login():
    """User login/appentication/session management."""
    error = None
    if request.method == "POST":
        if request.form["username"] != "admin":
            error = "Invalid username"
        elif request.form["password"] != "admin":
            error = "Invalid password"
        else:
            session["logged_in"] = True
            flash("You were logged in")
            return redirect(url_for("user_root"))
    return render_template("user/login.html", error=error)


@app.route("/user/logout/")
def logout():
    """User logout/appentication/session management."""
    session.pop("logged_in", None)
    flash("You were logged out")
    return redirect(url_for("user_root"))


@app.route("/user/delete/<int:post_id>/", methods=["GET"])
@login_required
def delete_entry(post_id):
    """Deletes post from database."""
    try:
        new_id = post_id
        db.session.query(models.Post).filter_by(id=new_id).delete()
        db.session.commit()
        result = {"status": 1, "message": "Post Deleted"}
        flash("The entry was deleted.")
        return jsonify(result)
    except Exception as e:
        return jsonify({"status": 0, "message": repr(e)})


@app.route("/user/search/", methods=["GET"])
def search():
    query = request.args.get("query")
    entries = db.session.query(models.Post)
    if query:
        return render_template("user/search.html", entries=entries, query=query)
    return render_template("user/search.html")
