from abc import abstractmethod
from typing import Tuple

from app.core.use_cases.use_case import BaseUseCase
from app.features.task.domain.entities.task_command_model import TaskCreateModel
from app.features.task.domain.entities.task_entity import TaskEntity
from app.features.task.domain.entities.task_query_model import TaskReadModel
from app.features.task.domain.repositories.task_unit_of_work import TaskUnitOfWork


class CreateTaskUseCase(BaseUseCase[Tuple[TaskCreateModel], TaskReadModel]):

    unit_of_work: TaskUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[TaskCreateModel]) -> TaskReadModel:
        raise NotImplementedError()


class CreateTaskUseCaseImpl(CreateTaskUseCase):

    def __init__(self, unit_of_work: TaskUnitOfWork):
        self.unit_of_work = unit_of_work

    def __call__(self, args: Tuple[TaskCreateModel]) -> TaskReadModel:
        data, = args

        task = TaskEntity(
            id_=None,
            **data.dict()
        )

        try:
            self.unit_of_work.repository.create(task)
        except Exception as _e:
            self.unit_of_work.rollback()
            raise

        self.unit_of_work.commit()

        created_task = self.unit_of_work.repository.find_by_owner_id(task.owner_id)[0]

        return TaskReadModel.from_entity(created_task)
