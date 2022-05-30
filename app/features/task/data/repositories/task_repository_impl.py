from typing import Sequence

from sqlalchemy import select, update, delete
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

    def create(self, entity: TaskEntity) -> TaskEntity:
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
        result: Task | None = self.session.get(Task, id_)

        if result is None:
            return None

        return result.to_entity()

    def update(self, entity: TaskEntity) -> TaskEntity:
        task = Task.from_entity(entity)
        update_data = task.to_dict()

        for key in [Task.updated_at.key, Task.created_at.key, Task.updated_at.key]:
            update_data.pop(key)

        statement = update(
            Task
        ).filter_by(
            id_=task.id_
        ).values(
            update_data
        ).returning(
            Task
        )

        task_mapping = self.session.execute(statement).mappings().one()
        result = Task(**task_mapping)

        return task.to_entity()

    def delete_by_id(self, id_: int) -> TaskEntity:
        statement = delete(
            Task
        ).filter_by(
            id_=id_
        ).returning(
            *Task.__table__.columns
        )

        result: Task = self.session.execute(statement).scalar_one()

        return result.to_entity()
