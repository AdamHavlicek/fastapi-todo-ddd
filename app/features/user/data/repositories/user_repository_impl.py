from typing import Sequence

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from app.features.user.domain.entities.user_entity import UserEntity
from app.features.user.data.models.user_model import UserModel
from app.features.user.domain.repositories.user_repository import UserRepository


class UserRepositoryImpl(UserRepository):
    """
        UserRepositoryImpl implements CRUD operations related User entity using SQLAlchemy
    """

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_email(self, email: int) -> UserEntity | None:
        statement = select(UserModel).filter_by(email=email)

        try:
            result: Sequence[UserModel] = self.session.execute(statement).one()
        except NoResultFound:
            return None

        return result[0].to_entity()

    def create(self, entity: UserEntity) -> UserEntity | None:
        user = UserModel.from_entity(entity)

        self.session.add(user)

        return user.to_entity()

    def findall(self) -> Sequence[UserEntity]:
        # TODO: add offset and limit
        statement = select(UserModel)

        try:
            result: Sequence[UserModel] = self.session.execute(statement).one()
        except NoResultFound:
            return []

        return [user.to_entity() for user in result]

    def find_by_id(self, id_: int) -> UserEntity | None:
        statement = select(UserModel).filter_by(id_=id_)

        try:
            result: Sequence[UserModel] = self.session.execute(statement).one()
        except NoResultFound:
            return None

        return result[0].to_entity()

    def update(self, entity: UserEntity) -> UserEntity | None:
        user = UserModel.from_entity(entity)
        statement = select(UserModel).filter_by(id_=user.id_)

        try:
            result: UserModel = self.session.execute(statement).one()
        except NoResultFound:
            return None

        # TODO: update user

    def delete_by_id(self, id_: int) -> UserEntity | None:
        statement = select(UserModel).filter_by(id_=id_)

        result = self.session.execute(statement).one()
        # TODO: set is_deleted and persist
