from abc import abstractmethod
from typing import Sequence

from core.user_cases.use_case import BaseUseCase
from features.task.domain.entities.task_query_model import TaskReadModel
from features.task.domain.services.task_query_service import TaskQueryService


class GetTasksUseCase(BaseUseCase):

    service: TaskQueryService = None

    def __init__(self, service: TaskQueryService):
        self.service: TaskQueryService = service

    @abstractmethod
    def __call__(self) -> Sequence[TaskReadModel]:
        raise NotImplementedError()


class GetTasksUseCaseImpl(GetTasksUseCase):

    def __call__(self) -> Sequence[TaskReadModel]:
        try:
            tasks = self.service.findall()
        except Exception:
            raise

        return tasks