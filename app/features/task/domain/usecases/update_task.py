from abc import abstractmethod
from typing import cast, Callable, Tuple

from app.core.error.task_exception import TaskNotFoundError
from app.core.use_cases.use_case import BaseUseCase
from app.features.task.domain.entities.task_command_model import TaskUpdateModel
from app.features.task.domain.entities.task_entity import TaskEntity
from app.features.task.domain.entities.task_query_model import TaskReadModel
from app.features.task.domain.repositories.task_unit_of_work import TaskUnitOfWork


class UpdateTaskUseCase(BaseUseCase[Tuple[int, TaskUpdateModel], TaskReadModel]):

    unit_of_work: TaskUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[int, TaskUpdateModel]) -> TaskReadModel:
        raise NotImplementedError()


class UpdateTaskUseCaseImpl(UpdateTaskUseCase):

    def __init__(self, unit_of_work: TaskUnitOfWork):
        self.unit_of_work = unit_of_work

    def __call__(self, args: Tuple[int, TaskUpdateModel]) -> TaskReadModel:
        id_, update_data = args
        existing_task = self.unit_of_work.repository.find_by_id(id_)

        if existing_task is None:
            raise TaskNotFoundError()

        update_entity = existing_task.update_entity(
            update_data,
            lambda task_data: task_data.dict(exclude_unset=True)
        )

        try:
            updated_task = self.unit_of_work.repository.update(update_entity)
            self.unit_of_work.commit()
        except Exception:
            self.unit_of_work.rollback()
            raise


        return TaskReadModel.from_entity(cast(TaskEntity, updated_task))
