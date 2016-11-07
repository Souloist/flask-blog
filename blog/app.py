from __future__ import absolute_import

from flask import (
    Flask,
    abort,
    redirect,
    render_template,
    request,
    url_for
)

from blog.models import meta
from blog.models.user import User

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static",
)

app.config.from_object("blog.config")

@app.teardown_appcontext
def shutdown_session(exception=None):
    meta.session.remove()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signup", methods=["POST"])
def signup():
    user = User(request.form["username"], request.form["message"])
    meta.session.add(user)
    meta.session.commit()
    return redirect(url_for("message", username=user.username))

@app.route("/message/<username>")
def message(username):
    user = (
        meta.session.query(User)
            .filter(User.username == username)
    ).first()

    if user is None:
        return abort(403)
    return render_template("message.html",
                           username=user.username, message=user.message)
