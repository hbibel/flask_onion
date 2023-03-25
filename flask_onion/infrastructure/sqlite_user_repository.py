from sqlite3 import Connection

from flask_onion.domain.model import User
from flask_onion.domain_services.user_repository import UserAlreadyExistsError, UserRepository


class SqliteUserRepository(UserRepository):
    def __init__(self, db: Connection) -> None:
        self._db = db

    def insert(self, user: User) -> None:
        try:
            self._db.execute(
                "INSERT INTO user (username, password) VALUES (?, ?)",
                (user.name, user.password_hash),
            )
            self._db.commit()
        except self._db.IntegrityError:
            raise UserAlreadyExistsError()
