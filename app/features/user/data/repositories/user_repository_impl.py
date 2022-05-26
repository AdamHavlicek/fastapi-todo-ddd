from typing import Sequence, NoReturn

from sqlalchemy import select, update, delete
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

    def find_by_email(self, email: str) -> UserEntity | None:
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
            result: Sequence[User] = self.session.execute(statement).scalars().all()
        except NoResultFound:
            return []

        return [user.to_entity() for user in result]

    def find_by_id(self, id_: int) -> UserEntity | None:
        result: User | None = self.session.get(User, id_)

        if result is None:
            return None

        return result.to_entity()

    def update(self, entity: UserEntity) -> UserEntity | None:
        user = User.from_entity(entity)
        update_data = user.to_dict()
        map(
            lambda key: update_data.pop(key),
            [User.updated_at.key, User.created_at.key]
        )

        statement = update(
            User
        ).filter_by(
            id_=user.id_
        ).values(
            update_data
        ).returning(
            *user.__table__.columns
        )

        result: User = self.session.execute(statement).scalar_one()

        return result.to_entity()

    def delete_by_id(self, id_: int) -> UserEntity | None:
        statement = delete(
            User
        ).filter_by(
            id_=id_
        ).returning(
            *User.__table__.columns
        )

        result: User = self.session.execute(statement).scalar_one()

        return result.to_entity()
