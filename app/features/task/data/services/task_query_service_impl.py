from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.features.task.data.models.task import Task
from app.features.task.domain.entities.task_query_model import TaskReadModel
from app.features.task.domain.services.task_query_service import TaskQueryService


class TaskQueryServiceImpl(TaskQueryService):

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, id_: int) -> TaskReadModel | None:
        result = self.session.get(Task, id_)

        if result is None:
            return None

        return result.to_read_model()

    def findall(self) -> Sequence[TaskReadModel]:
        # TODO: add offset and limit
        statement = select(Task)

        result = self.session.execute(statement).scalars().all()

        if len(result) == 0:
            return []

        return [task.to_read_model() for task in result]
