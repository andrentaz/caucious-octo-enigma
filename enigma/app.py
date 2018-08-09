import os

from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def index():
        return "Hello World"

    CORS(app, resources=r"/*", headers="Content-Type")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080)),
        debug=os.environ.get("DEBUG", False)
    )
