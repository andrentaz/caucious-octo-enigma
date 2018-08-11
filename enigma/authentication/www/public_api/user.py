import flask

from authentication.services.user import user_service


blueprint = flask.Blueprint("user", __name__)

@blueprint.route("/users", methods=["POST"])
def create_user():
    email = flask.request.json.get("email")
    password = flask.request.json.get("password")

    if None in [email, password]:
        flask.abort(400)

    try:
        user = user_service.create_user(email, password)
    except user_service.EmailAlreadyUsed:
        return flask.abort(400, description="email already used for other user")

    return flask.jsonify({
        "email": user.email
    })
