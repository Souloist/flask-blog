import datetime, functools, re, urllib

from flask import (
    Flask,
    abort,
    flash,
    Markup,
    redirect,
    render_template,
    request,
    Response,
    session,
    url_for
)

app = Flask(__name__)
app.config.from_object("config")

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
