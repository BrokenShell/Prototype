from flask import Flask, render_template

from app.authentication import Authentication

APP = Flask(__name__)


@APP.route("/")
def logout():
    return render_template("home.html", authenticated=False)


@APP.route("/admin")
@Authentication.login_required
def login():
    return render_template("home.html", authenticated=True)


@APP.route("/admin/data")
@Authentication.login_required
def data():
    return render_template("data.html", authenticated=True)


@APP.route("/admin/view")
@Authentication.login_required
def view():
    return render_template("view.html", authenticated=True)


@APP.route("/admin/model")
@Authentication.login_required
def model():
    return render_template("model.html", authenticated=True)
