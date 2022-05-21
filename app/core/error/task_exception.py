"""
    Task Exceptions
"""
from app.core.error.base_exception import BaseError


class TaskNotFoundError(BaseError):
    message = 'User does not exist.'


class TasksNotFoundError(BaseError):
    message = 'Users do not exist'


class TaskAlreadyExistsError(BaseError):
    message = 'User already exists'
