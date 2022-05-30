from abc import abstractmethod
from typing import cast, Tuple

from app.core.error.user_exception import UserAlreadyExistsError
from app.core.use_cases.use_case import BaseUseCase
from app.features.user.domain.entities.user_command_model import UserCreateModel
from app.features.user.domain.entities.user_entity import UserEntity
from app.features.user.domain.entities.user_query_model import UserReadModel
from app.features.user.domain.repositories.user_unit_of_work import UserUnitOfWork


class CreateUserUseCase(BaseUseCase[Tuple[UserCreateModel], UserReadModel]):

    unit_of_work: UserUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[UserCreateModel]) -> UserReadModel:
        raise NotImplementedError()


class CreateUserUseCaseImpl(CreateUserUseCase):

    def __init__(self, unit_of_work: UserUnitOfWork):
        self.unit_of_work = unit_of_work

    def __call__(self, args: Tuple[UserCreateModel]) -> UserReadModel:
        data, = args

        user = UserEntity(
            id_=None,
            **data.dict()
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
