import os

from flask import Flask

from . import auth, db


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "db.sqlite"),
    )

    os.makedirs(app.instance_path, exist_ok=True)
    db.init_app(app)

    app.register_blueprint(auth.bp)

    return app
