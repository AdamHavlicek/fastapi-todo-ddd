from typing import Sequence

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from features.task.data.models.task import Task
from features.task.domain.entities.task_entity import TaskEntity
from features.task.domain.repositories.task_repository import TaskRepository


class TaskRepositoryImpl(TaskRepository):

    def __init__(self, session: Session):
        self.session: Session = session

    def create(self, entity: TaskEntity) -> TaskEntity | None:
        task = Task.from_entity(entity)

        self.session.add(task)

        return task.to_entity()

    def findall(self) -> Sequence[TaskEntity]:
        # TODO: add offset and limit
        statement = select(Task)

        try:
            result: Sequence[Task] = self.session.execute(statement).scalars().all()
        except NoResultFound:
            return []

        return [task.to_entity() for task in result]

    def find_by_id(self, id_: int) -> TaskEntity | None:
        try:
            result = self.session.get(Task, id_).scalar_one()
        except NoResultFound:
            return None

        return result.to_entity()

    def update(self, entity: TaskEntity) -> TaskEntity | None:
        task = Task.from_entity(entity)

        try:
            result = self.session.get(Task, task.id_).scalar_one()
        except NoResultFound:
            return None

        # TODO: update user

    def delete_by_id(self, id_: int) -> TaskEntity | None:
        try:
            result = self.session.get(Task, id_).scalar_one()
        except NoResultFound:
            return None

        # TODO: set is_deleted and persist