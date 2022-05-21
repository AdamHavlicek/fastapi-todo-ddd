from sqlalchemy.orm import Session

from app.features.user.domain.repositories.user_repository import UserRepository
from app.features.user.domain.usecases.user_command_unit_of_work import UserCommandUnitOfWork


class UserCommandUnitOfWorkImpl(UserCommandUnitOfWork):
    """"""

    def __init__(self, session: Session, user_repository: UserRepository):
        self.session: Session = session
        self.repository: UserRepository = user_repository

    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
