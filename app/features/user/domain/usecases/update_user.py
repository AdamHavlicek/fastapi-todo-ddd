from abc import abstractmethod
from typing import cast, Tuple, Optional

from app.core.error.user_exception import UserNotFoundError
from app.core.use_cases.use_case import BaseUseCase
from app.features.user.domain.entities.user_command_model import UserUpdateModel
from app.features.user.domain.entities.user_entity import UserEntity
from app.features.user.domain.entities.user_query_model import UserReadModel
from app.features.user.domain.repositories.user_unit_of_work import UserUnitOfWork


class UpdateUserUseCase(BaseUseCase[Tuple[int, UserUpdateModel], UserReadModel]):
    unit_of_work: UserUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[int, UserUpdateModel]) -> UserReadModel:
        raise NotImplementedError()


class UpdateUserUseCaseImpl(UpdateUserUseCase):

    def __init__(self, unit_of_work: UserUnitOfWork):
        self.unit_of_work = unit_of_work

    def __call__(self, args: Tuple[int, UserUpdateModel]) -> UserReadModel:
        id_, update_data = args

        existing_user: Optional[UserEntity] = self.unit_of_work.repository.find_by_id(id_)

        if existing_user is None:
            raise UserNotFoundError()

        update_entity = existing_user.update_entity(
            update_data,
            lambda user_data: update_data.dict(exclude_unset=True)
        )

        try:
            updated_user = self.unit_of_work.repository.update(update_entity)
            self.unit_of_work.commit()
        except Exception as e:
            self.unit_of_work.rollback()
            raise

        return UserReadModel.from_entity(cast(UserEntity, updated_user))
