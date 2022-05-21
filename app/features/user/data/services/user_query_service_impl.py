from typing import Sequence

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from app.features.user.data.models.user import User
from app.features.user.domain.entities.user_query_model import UserReadModel
from app.features.user.domain.services.user_query_service import UserQueryService


class UserQueryServiceImpl(UserQueryService):
    """
        UserQueryServiceImpl implements READ operations related to User entity using SQLALCHEMY
    """

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, id_: int) -> UserReadModel | None:
        statement = select(User).filter_by(id_=id_)

        try:
            result: User = self.session.execute(statement).scalars().one()
        except NoResultFound:
            return None

        return result.to_read_model()

    def findall(self) -> Sequence[UserReadModel]:
        # TODO: add offset and limit
        statement = select(User)

        result = self.session.execute(statement).scalars().all()

        if len(result) == 0:
            return []

        return [user.to_read_model() for user in result]
