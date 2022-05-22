from abc import abstractmethod
from typing import cast

from core.error.task_exception import TaskNotFoundError
from core.user_cases.use_case import BaseUseCase
from features.task.domain.entities.task_command_model import TaskUpdateModel
from features.task.domain.entities.task_entity import TaskEntity
from features.task.domain.entities.task_query_model import TaskReadModel
from features.task.domain.repositories.task_unit_of_work import TaskUnitOfWork


class UpdateTaskUseCase(BaseUseCase):

    unit_of_work: TaskUnitOfWork

    def __init__(self, unit_of_work: TaskUnitOfWork):
        self.unit_of_work = unit_of_work

    @abstractmethod
    def __call__(self, id_: int, data: TaskUpdateModel) -> TaskReadModel | None:
        raise NotImplementedError()


class UpdateTaskUseCaseImpl(UpdateTaskUseCase):

    def __call__(self, id_: int, data: TaskUpdateModel) -> TaskReadModel | None:
        existing_task = self.unit_of_work.repository.find_by_id(id_)

        if existing_task is None:
            raise TaskNotFoundError()

        task = TaskEntity(
            **dict(existing_task),
            **dict(data)
        )

        try:
            updated_task = self.unit_of_work.repository.update(task)
        except Exception:
            self.unit_of_work.rollback()
            raise

        self.unit_of_work.commit()

        return TaskReadModel.from_entity(cast(TaskEntity, updated_task))
