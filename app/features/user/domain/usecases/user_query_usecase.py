from abc import ABC, abstractmethod
from typing import Sequence

from app.features.user.domain.usecases.user_query_model import UserReadModel
from app.features.user.domain.usecases.user_query_service import UserQueryService
from app.core.error.user_exception import UserNotFoundError


class UserQueryUseCase(ABC):
    """
        UserQueryUseCase defines a query use case interface related User Entity
    """

    @abstractmethod
    def fetch_user_by_id(self, id_: int) -> UserReadModel | None:
        raise NotImplementedError()

    @abstractmethod
    def fetch_users(self) -> Sequence[UserReadModel]:
        raise NotImplementedError()


class UserQueryUseCaseImpl(UserQueryUseCase):
    """
        UserQueryUseCaseImpl implements a query use cases related to User entity
    """

    def __init__(self, service: UserQueryService):
        self.service: UserQueryService = service

    def fetch_user_by_id(self, id_: int) -> UserReadModel | None:
        try:
            user = self.service.find_by_id(id_)
            if user is None:
                raise UserNotFoundError
        except Exception:
            raise

        return user

    def fetch_users(self) -> Sequence[UserReadModel]:
        try:
            users = self.service.findall()
        except Exception:
            raise

        return users
