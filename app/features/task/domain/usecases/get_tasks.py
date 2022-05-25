from abc import abstractmethod
from typing import Sequence

from app.core.use_cases.use_case import BaseUseCase
from app.features.task.domain.entities.task_query_model import TaskReadModel
from app.features.task.domain.services.task_query_service import TaskQueryService


class GetTasksUseCase(BaseUseCase[None, Sequence[TaskReadModel]]):

    service: TaskQueryService

    @abstractmethod
    def __call__(self, args: None) -> Sequence[TaskReadModel]:
        raise NotImplementedError()


class GetTasksUseCaseImpl(GetTasksUseCase):

    def __init__(self, service: TaskQueryService):
        self.service: TaskQueryService = service

    def __call__(self, args: None) -> Sequence[TaskReadModel]:
        try:
            tasks = self.service.findall()
        except Exception:
            raise

        return tasks