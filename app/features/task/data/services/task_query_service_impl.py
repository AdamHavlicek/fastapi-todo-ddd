from typing import Sequence

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from features.task.data.models.task import Task
from features.task.domain.entities.task_entity import TaskEntity
from features.task.domain.services.task_query_service import TaskQueryService


class TaskQueryServiceImpl(TaskQueryService):

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, id_: int) -> TaskEntity | None:
        try:
            result: Task = self.session.get(Task, id_).scalar_one()
        except NoResultFound:
            return None

        return result.to_entity()

    def findall(self) -> Sequence[TaskEntity]:
        # TODO: add offset and limit
        statement = select(Task)

        result = self.session.execute(statement).scalars().all()

        if len(result) == 0:
            return []

        return [task.to_read_model() for task in result]
