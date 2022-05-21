from abc import abstractmethod

from app.core.repository import AbstractRepository
from app.features.user.domain.entities.user_entity import UserEntity


class UserRepository(AbstractRepository[UserEntity]):
    """UserRepository defines a repository interface for User entity"""

    @abstractmethod
    def find_by_email(self, email: str) -> UserEntity | None:
        raise NotImplementedError()

