from flask import Blueprint

helloWorldRoutes = Blueprint("helloWorldRoutes", __name__)


@helloWorldRoutes.route("/helloWorld")
def helloWorld():
    return "Hello mundito! 😊"
