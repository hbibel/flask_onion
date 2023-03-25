import os
from typing import Callable

import click
from flask import Flask

from flask_onion.app.auth import AuthModule
from flask_onion.application_services.user_service import UserService
from flask_onion.infrastructure.sqlite_db import SqliteDb
from flask_onion.infrastructure.sqlite_user_repository import SqliteUserRepository


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(SECRET_KEY="dev")

    os.makedirs(app.instance_path, exist_ok=True)
    sqlite_db = SqliteDb("db.sqlite", lambda: app.open_resource("../infrastructure/schema.sql"))
    app.cli.add_command(init_db_command(sqlite_db))

    user_service = UserService(SqliteUserRepository(sqlite_db.connection))

    auth_module = AuthModule(user_service)
    app.register_blueprint(auth_module.blueprint)

    return app


def init_db_command(db_: SqliteDb) -> Callable[[], None]:
    @click.command("init-db")
    def f():
        db_.init_db()
        click.echo("Initialized the database.")

    return f
