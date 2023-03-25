from werkzeug.security import generate_password_hash

from flask_onion.domain.model import User
from flask_onion.domain_services.user_repository import UserAlreadyExistsError, UserRepository


class UserService:
    def __init__(self, user_repo: UserRepository) -> None:
        self._user_repo = user_repo

    def create_and_insert_user(self, username: str, password: str) -> str | None:
        error: str | None = None
        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."

        user = User(username, generate_password_hash(password))
        try:
            self._user_repo.insert(user)
        except UserAlreadyExistsError:
            error = f"User {username} already exists"

        return error
