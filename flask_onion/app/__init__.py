from typing import Callable

import click
from fastapi import FastAPI

from flask_onion.app import auth
from flask_onion.infrastructure.sqlite_db import SqliteDb


def create_app():
    app = FastAPI()

    # This concept doesn't map 1:1 in FastAPI;
    # app.cli.add_command(init_db_command(sqlite_db))

    app.include_router(auth.router)

    return app


def init_db_command(db_: SqliteDb) -> Callable[[], None]:
    @click.command("init-db")
    def f():
        db_.init_db()
        click.echo("Initialized the database.")

    return f
