from abc import ABC, abstractmethod

from flask_onion.domain.model import User


class UserRepository(ABC):
    @abstractmethod
    def insert(self, user: User) -> None:
        """Should raise UserAlreadyExistsError if user already exists."""
        ...


class UserAlreadyExistsError(Exception):
    pass
