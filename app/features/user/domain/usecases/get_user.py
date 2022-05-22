from abc import abstractmethod

from app.core.user_cases.use_case import BaseUseCase
from app.features.user.domain.entities.user_query_model import UserReadModel
from app.features.user.domain.services.user_query_service import UserQueryService
from app.core.error.user_exception import UserNotFoundError


class GetUserUseCase(BaseUseCase):
    """
        GetUserUseCase defines a query use case interface related User Entity
    """

    service: UserQueryService = None

    def __init__(self, service: UserQueryService):
        self.service: UserQueryService = service

    @abstractmethod
    def __call__(self, id_: int) -> UserReadModel | None:
        raise NotImplementedError()


class GetUserUseCaseImpl(GetUserUseCase):
    """
        GetUserUseCaseImpl implements a query use cases related to User entity
    """

    def __call__(self, id_: int) -> UserReadModel | None:
        try:
            user = self.service.find_by_id(id_)
            if user is None:
                raise UserNotFoundError()
        except Exception:
            raise

        return user

