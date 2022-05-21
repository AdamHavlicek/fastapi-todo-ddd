from typing import Sequence

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from app.features.user.data.models.user_model import UserModel
from app.features.user.domain.usecases.user_query_model import UserReadModel
from app.features.user.domain.usecases.user_query_service import UserQueryService


class UserQueryServiceImpl(UserQueryService):
    """
        UserQueryServiceImpl implements READ operations related to User entity using SQLALCHEMY
    """

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, id_: int) -> UserReadModel | None:
        statement = select(UserModel).filter_by(id_=id_)

        try:
            result: UserModel = self.session.execute(statement).one()
        except NoResultFound:
            return None

        return result[0].to_read_model()

    def findall(self) -> Sequence[UserReadModel]:
        # TODO: add offset and limit
        statement = select(UserModel)

        try:
            result: Sequence[UserModel] = self.session.execute(statement).one()
        except NoResultFound:
            return []

        return [user.to_read_model() for user in result]
