from sqlalchemy.orm import Session

from app.features.task.domain.repositories.task_repository import TaskRepository
from app.features.task.domain.repositories.task_unit_of_work import TaskUnitOfWork


class TaskUnitOfWorkImpl(TaskUnitOfWork):

    def __init__(self, session: Session, repository: TaskRepository):
        self.session: Session = session
        self.repository: TaskRepository = repository

    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
