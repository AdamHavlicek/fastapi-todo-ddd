from abc import abstractmethod
from typing import cast, Tuple

from app.core.error.user_exception import UserNotFoundError
from app.features.user.domain.entities.user_entity import UserEntity
from app.features.user.domain.entities.user_query_model import UserReadModel
from app.features.user.domain.repositories.user_unit_of_work import UserUnitOfWork
from app.core.use_cases.use_case import BaseUseCase


class DeleteUserUseCase(BaseUseCase[Tuple[int], UserReadModel]):
    """
        UserCommandUseCase defines a command use case interface related User entity
    """
    unit_of_work: UserUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[int]) -> UserReadModel:
        raise NotImplementedError()


class DeleteUserUseCaseImpl(DeleteUserUseCase):
    """
        UserCommandUseCaseImpl implements a command use cases related to the User entity
    """

    def __init__(self, unit_of_work: UserUnitOfWork):
        self.unit_of_work: UserUnitOfWork = unit_of_work

    def __call__(self, args: Tuple[int]) -> UserReadModel:
        id_, = args
        existing_user = self.unit_of_work.repository.find_by_id(id_)

        if existing_user is None:
            raise UserNotFoundError()

        marked_user = existing_user.mark_entity_as_deleted()

        try:
            deleted_user = self.unit_of_work.repository.update(marked_user)
            self.unit_of_work.commit()
        except Exception as e:
            self.unit_of_work.rollback()
            raise

        return UserReadModel.from_entity(cast(UserEntity, deleted_user))
