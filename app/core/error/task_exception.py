"""
    Task Exceptions
"""
from app.core.error.base_exception import BaseError


class TaskNotFoundError(BaseError):
    message = 'Task does not exist.'


class TasksNotFoundError(BaseError):
    message = 'Tasks do not exist'


class TaskAlreadyExistsError(BaseError):
    message = 'Task already exists'
