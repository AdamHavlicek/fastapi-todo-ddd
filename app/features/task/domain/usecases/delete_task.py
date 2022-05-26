from abc import abstractmethod
from typing import cast, Tuple

from app.core.error.task_exception import TaskNotFoundError
from app.core.use_cases.use_case import BaseUseCase
from app.features.task.domain.entities.task_entity import TaskEntity
from app.features.task.domain.entities.task_query_model import TaskReadModel
from app.features.task.domain.repositories.task_unit_of_work import TaskUnitOfWork


class DeleteTaskUseCase(BaseUseCase):
    unit_of_work: TaskUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[int]) -> TaskReadModel:
        raise NotImplementedError()


class DeleteTaskUseCaseImpl(DeleteTaskUseCase):

    def __init__(self, unit_of_work: TaskUnitOfWork):
        self.unit_of_work: TaskUnitOfWork = unit_of_work

    def __call__(self, args: Tuple[int]) -> TaskReadModel:
        id_, = args

        existing_user = self.unit_of_work.repository.find_by_id(id_)

        if existing_user is None:
            raise TaskNotFoundError()

        marked_task = existing_user.mark_entity_as_deleted()

        try:
            deleted_user = self.unit_of_work.repository.update(marked_task)
            self.unit_of_work.commit()
        except Exception:
            self.unit_of_work.rollback()
            raise

        return TaskReadModel.from_entity(cast(TaskEntity, deleted_user))
