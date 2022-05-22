from core.unit_of_work.unit_of_work import AbstractUnitOfWork
from features.task.domain.repositories.task_repository import TaskRepository


class TaskUnitOfWork(AbstractUnitOfWork[TaskRepository]):
    pass
