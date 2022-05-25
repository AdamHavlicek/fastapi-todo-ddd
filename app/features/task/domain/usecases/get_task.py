from abc import abstractmethod
from typing import Tuple

from app.core.error.task_exception import TaskNotFoundError
from app.core.use_cases.use_case import BaseUseCase
from app.features.task.domain.entities.task_query_model import TaskReadModel
from app.features.task.domain.services.task_query_service import TaskQueryService


class GetTaskUseCase(BaseUseCase[Tuple[int], TaskReadModel]):

    service: TaskQueryService

    @abstractmethod
    def __call__(self, args: Tuple[int]) -> TaskReadModel:
        raise NotImplementedError()


class GetTaskUseCaseImpl(GetTaskUseCase):

    def __init__(self, service: TaskQueryService):
        self.service: TaskQueryService = service

    def __call__(self, args: Tuple[int]) -> TaskReadModel:
        id_, = args
        try:
            task = self.service.find_by_id(id_)
            if task is None:
                raise TaskNotFoundError()
        except Exception:
            raise

        return task