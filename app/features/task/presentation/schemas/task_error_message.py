from pydantic import BaseModel, Field

from app.core.error.task_exception import TaskNotFoundError, TasksNotFoundError


class ErrorMessageTaskNotFound(BaseModel):
    detail: str = Field(example=TaskNotFoundError.message)


class ErrorMessageTasksNotFound(BaseModel):
    detail: str = Field(example=TasksNotFoundError.message)

