from __future__ import absolute_import

from flask import (
    Flask,
    abort,
    redirect,
    render_template,
    request,
    session,
    url_for
)
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config")

db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signup", methods=["POST"])
def signup():
    session["username"] = request.form["username"]
    session["message"] = request.form["message"]
    return redirect(url_for("message"))

@app.route("/message")
def message():
    if not "username" in session:
        return abort(403)
    return render_template("message.html", username=session["username"],
                                           message=session["message"])
