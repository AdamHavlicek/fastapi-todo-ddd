from abc import abstractmethod

from core.error.task_exception import TaskNotFoundError
from core.user_cases.use_case import BaseUseCase
from features.task.domain.entities.task_query_model import TaskReadModel
from features.task.domain.services.task_query_service import TaskQueryService


class GetTaskUseCase(BaseUseCase):

    service: TaskQueryService = None

    def __init__(self, service: TaskQueryService):
        self.service: TaskQueryService = service

    @abstractmethod
    def __call__(self, id_: int) -> TaskReadModel | None:
        raise NotImplementedError()


class GetTaskUseCaseImpl(GetTaskUseCase):

    def __call__(self, id_: int) -> TaskReadModel | None:
        try:
            task = self.service.find_by_id(id_)
            if task is None:
                raise TaskNotFoundError()
        except Exception:
            raise

        return task