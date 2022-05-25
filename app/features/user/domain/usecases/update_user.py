from abc import abstractmethod
from typing import cast

from app.core.error.user_exception import UserNotFoundError
from app.core.use_cases.use_case import BaseUseCase
from app.features.user.domain.entities.user_command_model import UserUpdateModel
from app.features.user.domain.entities.user_entity import UserEntity
from app.features.user.domain.entities.user_query_model import UserReadModel
from app.features.user.domain.repositories.user_unit_of_work import UserUnitOfWork


class UpdateUserUseCase(BaseUseCase):

    unit_of_work: UserUnitOfWork

    def __init__(self, unit_of_work: UserUnitOfWork):
        self.unit_of_work = unit_of_work

    @abstractmethod
    def __call__(self, id_: int, data: UserUpdateModel) -> UserReadModel | None:
        raise NotImplementedError()


class UpdateUserUseCaseImpl(UpdateUserUseCase):

    def __call__(self, id_: int, data: UserUpdateModel) -> UserReadModel | None:
        existing_user = self.unit_of_work.repository.find_by_id(id_)

        if existing_user is None:
            raise UserNotFoundError()

        user = UserEntity(
            **dict(existing_user),
            **dict(data)
        )

        try:
            updated_user = self.unit_of_work.repository.update(user)
        except Exception:
            self.unit_of_work.rollback()
            raise

        self.unit_of_work.commit()

        return UserReadModel.from_entity(cast(UserEntity, updated_user))
