from fastapi import Depends
from sqlalchemy.orm import Session

from features.task.data.repositories.task_repository_impl import TaskRepositoryImpl
from features.task.data.repositories.task_unit_of_work_impl import TaskUnitOfWorkImpl
from features.task.data.services.task_query_service_impl import TaskQueryServiceImpl
from features.task.domain.repositories.task_repository import TaskRepository
from features.task.domain.repositories.task_unit_of_work import TaskUnitOfWork
from features.task.domain.services.task_query_service import TaskQueryService
from features.task.domain.usecases.create_task import CreateTaskUseCase, CreateTaskUseCaseImpl
from features.task.domain.usecases.delete_task import DeleteTaskUseCase, DeleteTaskUseCaseImpl
from features.task.domain.usecases.get_task import GetTaskUseCase, GetTaskUseCaseImpl
from features.task.domain.usecases.get_tasks import GetTasksUseCase, GetTasksUseCaseImpl
from features.task.domain.usecases.update_task import UpdateTaskUseCase, UpdateTaskUseCaseImpl
from core.database.postgres import get_session


def get_task_query_service(
    session: Session = Depends(get_session)
) -> TaskQueryService:
    return TaskQueryServiceImpl(session)


def get_task_repository(session: Session = Depends(get_session)) -> TaskRepository:
    return TaskRepositoryImpl(session)


def get_task_unit_of_work(
    session: Session = Depends(get_session),
    task_repository: TaskRepository = Depends(get_task_repository)
) -> TaskUnitOfWork:
    return TaskUnitOfWorkImpl(session, task_repository)


def get_tasks_use_case(
    task_query_service: TaskQueryService = Depends(get_task_query_service)
) -> GetTasksUseCase:
    return GetTasksUseCaseImpl(task_query_service)


def get_create_task_use_case(
    task_unit_of_work: TaskUnitOfWork = Depends(get_task_unit_of_work)
) -> CreateTaskUseCase:
    return CreateTaskUseCaseImpl(task_unit_of_work)


def get_delete_task_use_case(
    task_unit_of_work: TaskUnitOfWork = Depends(get_task_unit_of_work)
) -> DeleteTaskUseCase:
    return DeleteTaskUseCaseImpl(task_unit_of_work)


def get_task_use_case(
    task_query_service: TaskQueryService = Depends(get_task_query_service)
) -> GetTaskUseCase:
    return GetTaskUseCaseImpl(task_query_service)


def get_update_task_use_case(
    task_unit_of_work: TaskUnitOfWork = Depends(get_task_unit_of_work)
) -> UpdateTaskUseCase:
    return UpdateTaskUseCaseImpl(task_unit_of_work)
