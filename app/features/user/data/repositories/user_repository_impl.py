from typing import Sequence

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from app.features.user.domain.entities.user_entity import UserEntity
from app.features.user.data.models.user import User
from app.features.user.domain.repositories.user_repository import UserRepository


class UserRepositoryImpl(UserRepository):
    """
        UserRepositoryImpl implements CRUD operations related User entity using SQLAlchemy
    """

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_email(self, email: int) -> UserEntity | None:
        statement = select(User).filter_by(email=email)

        try:
            result: User = self.session.execute(statement).scalar_one()
        except NoResultFound:
            return None

        return result.to_entity()

    def create(self, entity: UserEntity) -> UserEntity | None:
        user = User.from_entity(entity)

        self.session.add(user)

        return user.to_entity()

    def findall(self) -> Sequence[UserEntity]:
        # TODO: add offset and limit
        statement = select(User)

        try:
            result: Sequence[User] = self.session.execute(statement).scalar_one()
        except NoResultFound:
            return []

        return [user.to_entity() for user in result]

    def find_by_id(self, id_: int) -> UserEntity | None:
        try:
            result = self.session.get(User, id_)
        except NoResultFound:
            return None

        return result.to_entity()

    def update(self, entity: UserEntity) -> UserEntity | None:
        user = User.from_entity(entity)
        statement = select(User).filter_by(id_=user.id_)

        try:
            result: User = self.session.execute(statement).scalar_one()
        except NoResultFound:
            return None

        # TODO: update user

    def delete_by_id(self, id_: int) -> UserEntity | None:
        statement = select(User).filter_by(id_=id_)

        result: User = self.session.execute(statement).scalar_one()
        # TODO: set is_deleted and persist
