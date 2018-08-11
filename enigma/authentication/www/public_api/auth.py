import flask

from flask import current_app as app
from authentication.services.user import user_service
from authentication.services.auth import auth_service


blueprint = flask.Blueprint("auth", __name__)

@blueprint.route("/token", methods=["POST"])
def create_token():
    body = flask.request.json
    email = body.get("email")
    password = body.get("password")

    if not user_service.verify_password(email, password):
        flask.abort(401)

    user = user_service.get_user(email)
    secret_key = app.config["SECRET_KEY"]
    ttl = app.config["TOKEN_EXPIRATION_TTL"]
    token = auth_service.generate_auth_token(user=user, secret_key=secret_key, ttl=ttl)

    return flask.jsonify({
        "token": token.decode("ascii"),
        "expires_in": ttl,
    })


@blueprint.route("/me", methods=["GET"])
def authme():
    auth_header = flask.request.headers.get("Authorization")

    if not auth_header:
        flask.abort(401)

    auth_header_data = auth_header.split(" ")

    if len(auth_header_data) != 2:
        flask.abort(401, description="Missing authentication headers")

    auth_method = auth_header_data[0]
    token = auth_header_data[-1]

    if auth_method != "Bearer":
        flask.abort(401, description="Missing authentication headers")

    user = auth_service.verify_auth_token(token=token, secret_key=app.config["SECRET_KEY"])

    if user:
        return flask.jsonify({
            "email": user.email
        })

    flask.abort(404, description="No user found with the given token")


