from abc import abstractmethod

from core.user_cases.use_case import BaseUseCase
from features.task.domain.entities.task_command_model import TaskCreateModel
from features.task.domain.entities.task_entity import TaskEntity
from features.task.domain.entities.task_query_model import TaskReadModel
from features.task.domain.repositories.task_unit_of_work import TaskUnitOfWork


class CreateTaskUseCase(BaseUseCase):

    unit_of_work: TaskUnitOfWork = None

    def __init__(self, unit_of_work: TaskUnitOfWork):
        self.unit_of_work = unit_of_work

    @abstractmethod
    def __call__(self, data: TaskCreateModel) -> TaskReadModel | None:
        raise NotImplementedError()


class CreateTaskUseCaseImpl(CreateTaskUseCase):

    def __call__(self, data: TaskCreateModel) -> TaskReadModel | None:
        task = TaskEntity(
            id_=-1,
            title=data.title,
            owner_id=data.owner_id
        )

        try:
            created_task = self.unit_of_work.repository.create(task)
        except Exception as _e:
            self.unit_of_work.rollback()
            raise

        self.unit_of_work.commit()

        return TaskReadModel.from_entity(created_task)