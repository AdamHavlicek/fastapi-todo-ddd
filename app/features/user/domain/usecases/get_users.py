from abc import abstractmethod
from typing import Sequence

from app.core.use_cases.use_case import BaseUseCase
from app.features.user.domain.entities.user_query_model import UserReadModel
from app.features.user.domain.services.user_query_service import UserQueryService


class GetUsersUseCase(BaseUseCase):

    service: UserQueryService

    def __init__(self, service: UserQueryService):
        self.service: UserQueryService = service

    @abstractmethod
    def __call__(self) -> Sequence[UserReadModel]:
        raise NotImplementedError()


class GetUsersUseCaseImpl(GetUsersUseCase):

    def __call__(self) -> Sequence[UserReadModel]:
        try:
            users = self.service.findall()
        except Exception:
            raise

        return users