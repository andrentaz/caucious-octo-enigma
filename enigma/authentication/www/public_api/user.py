import flask

from authentication.services.user import user_service


blueprint = flask.Blueprint("users", __name__)

@blueprint.route("/users", methods=["POST"])
def create_user():
    username = flask.request.json.get("username")
    password = flask.request.json.get("password")

    if None in [username, password]:
        flask.abort(400)

    user = user_service.create_user(username, password)

    return flask.jsonify({
        "username": user.username
    })
