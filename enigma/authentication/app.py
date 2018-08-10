import os

from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    # setup endpoints
    import authentication.www.public_api.index
    import authentication.www.public_api.user

    app.register_blueprint(
        authentication.www.public_api.index.blueprint,
    )
    app.register_blueprint(
        authentication.www.public_api.user.blueprint,
        url_prefix="/api"
    )
    CORS(app, resources=r"/*", headers="Content-Type")

    # setup mongo
    from authentication import mongo
    mongo.setup_connection(mongo_uri=os.environ["MONGO_URI"])

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080)),
        debug=os.environ.get("DEBUG", False)
    )
