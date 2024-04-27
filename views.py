from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html")

@views.route("/about")
def about():
    return render_template("about.html")

@views.route("/site")
def site():
    return render_template("site.html")

@views.route("/contact")
def contact():
    return render_template("contact.html")

@views.route("/post")
def post():
    return render_template("post.html")

@views.route("/post_f1")
def post_f1():
    return render_template("post_f1.html")

@views.route("/post_urm")
def post_urm():
    return render_template("post_urm.html")

@views.route("/post_baseball")
def post_baseball():
    return render_template("post_baseball.html")

@views.route("/post_wikipedia")
def post_wikipedia():
    return render_template("post_wikipedia.html")

@views.route("/post_fpforce")
def post_fpforce():
    return render_template("post_fpforce.html")

@views.route("/post_strava")
def post_strava():
    return render_template("post_strava.html")