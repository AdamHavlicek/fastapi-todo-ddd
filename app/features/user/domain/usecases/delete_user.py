from abc import abstractmethod
from typing import cast

from app.core.error.user_exception import UserNotFoundError
from app.features.user.domain.entities.user_entity import UserEntity
from app.features.user.domain.entities.user_query_model import UserReadModel
from app.features.user.domain.repositories.user_unit_of_work import UserUnitOfWork
from app.core.use_cases.use_case import BaseUseCase


class DeleteUserUseCase(BaseUseCase):
    """
        UserCommandUseCase defines a command use case interface related User entity
    """
    unit_of_work: UserUnitOfWork

    def __init__(self, unit_of_work: UserUnitOfWork):
        self.unit_of_work: UserUnitOfWork = unit_of_work

    @abstractmethod
    def __call__(self, id_: int) -> UserReadModel | None:
        raise NotImplementedError()


class DeleteUserUseCaseImpl(DeleteUserUseCase):
    """
        UserCommandUseCaseImpl implements a command use cases related to the User entity
    """

    def __call__(self, id_: int) -> UserReadModel | None:
        try:
            existing_user = self.unit_of_work.repository.find_by_id(id_)

            if existing_user is None:
                raise UserNotFoundError()

            deleted_user = self.unit_of_work.repository.delete_by_id(id_)

            self.unit_of_work.commit()

        except Exception:
            self.unit_of_work.rollback()
            raise

        return UserReadModel.from_entity(cast(UserEntity, deleted_user))
