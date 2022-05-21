from abc import ABC, abstractmethod
from typing import cast

from app.features.user.domain.entities.user_entity import UserEntity
from app.features.user.domain.usecases.user_command_model import UserCreateModel, UserUpdateModel
from app.features.user.domain.usecases.user_command_unit_of_work import UserCommandUnitOfWork
from app.features.user.domain.usecases.user_query_model import UserReadModel
from app.core.error.user_exception import UserAlreadyExistsError, UserNotFoundError


class UserCommandUseCase(ABC):
    """
        UserCommandUseCase defines a command use case interface related User entity
    """

    @abstractmethod
    def create_user(self, data: UserCreateModel) -> UserReadModel | None:
        raise NotImplementedError()

    @abstractmethod
    def update_user(self, id_: int, data: UserCreateModel) -> UserReadModel | None:
        raise NotImplementedError()

    @abstractmethod
    def delete_user_by_id(self, id_: int) -> UserReadModel | None:
        raise NotImplementedError()


class UserCommandUseCaseImpl(UserCommandUseCase):
    """
        UserCommandUseCaseImpl implements a command use cases related to the User entity
    """

    def __init__(self, unit_of_work: UserCommandUnitOfWork):
        self.unit_of_work: UserCommandUnitOfWork = unit_of_work

    def create_user(self, data: UserCreateModel) -> UserReadModel | None:
        user = UserEntity(
            id_=-1,
            email=data.email,
            password=data.password,
        )

        existing_user = self.unit_of_work.repository.find_by_email(data.email)
        if existing_user is not None:
            raise UserAlreadyExistsError()

        try:
            self.unit_of_work.repository.create(user)
        except Exception as _e:
            self.unit_of_work.rollback()
            raise

        self.unit_of_work.commit()

        created_user = self.unit_of_work.repository.find_by_email(data.email)

        return UserReadModel.from_entity(cast(UserEntity, created_user))

    def update_user(self, id_: int, data: UserUpdateModel) -> UserReadModel | None:
        try:
            existing_user = self.unit_of_work.repository.find_by_id(id_)

            if existing_user is None:
                raise UserNotFoundError()

            user = UserEntity(
                **dict(existing_user),
                **dict(data)
            )

            updated_user = self.unit_of_work.repository.update(user)

            self.unit_of_work.commit()
        except Exception:
            self.unit_of_work.rollback()
            raise

        return UserReadModel.from_entity(cast(UserEntity, updated_user))

    def delete_user_by_id(self, id_: int) -> UserReadModel | None:
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
