from flask import Blueprint, render_template

core = Blueprint(
    "core",
    __name__,
    url_prefix="",
    template_folder="templates/core/",
    static_folder="static"
)


@core.app_errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@core.route('/')
@core.route('/home')
def get_home():
    # return "Welcome to efecto pez"
    return render_template("index.html")


@core.route('/about')
@core.route('/que-es-efecto-pez')
def get_about():
    # return "Efecto pez es un portal web de divulgación científica que tiene como objetivo democratizar la ciencia"
    return render_template("about.html")
