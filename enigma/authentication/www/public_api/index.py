from flask import Blueprint

blueprint = Blueprint("index", __name__)

@blueprint.route("/", methods=["GET"])
def index():
    return "Hello World"
