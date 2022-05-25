from typing import Sequence

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from app.features.task.data.models.task import Task
from app.features.task.domain.entities.task_entity import TaskEntity
from app.features.task.domain.repositories.task_repository import TaskRepository


class TaskRepositoryImpl(TaskRepository):

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_owner_id(self, owner_id: int) -> Sequence[TaskEntity]:
        statement = select(Task).filter_by(owner_id=owner_id).order_by(Task.created_at.desc())

        try:
            result: Sequence[Task] = self.session.execute(statement).scalars().all()
        except NoResultFound:
            return []

        return [task.to_entity() for task in result]

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
        result = self.session.get(Task, id_)

        if result is None:
            return None

        return result.to_entity()

    def update(self, entity: TaskEntity) -> TaskEntity | None:
        task = Task.from_entity(entity)

        try:
            result = self.session.get(Task, task.id_)
        except NoResultFound:
            return None

        raise NotImplementedError()

        # TODO: update user

    def delete_by_id(self, id_: int) -> TaskEntity | None:
        try:
            result = self.session.get(Task, id_)
        except NoResultFound:
            return None

        raise NotImplementedError()

        # TODO: set is_deleted and persist