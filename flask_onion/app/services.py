from typing import Annotated

from fastapi import Depends

from flask_onion.application_services.user_service import UserService
from flask_onion.infrastructure.sqlite_db import SqliteDb
from flask_onion.infrastructure.sqlite_user_repository import SqliteUserRepository


def get_db():
    db = SqliteDb("db.sqlite", lambda: open("../infrastructure/schema.sql"))
    try:
        yield db
    finally:
        db.connection.close()


def get_user_service(sqlite_db: Annotated[SqliteDb, Depends(get_db)]):
    return UserService(SqliteUserRepository(sqlite_db.connection))
