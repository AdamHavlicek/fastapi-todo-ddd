from pydantic import BaseModel, Field

from app.core.error.user_exception import (
    UserNotFoundError,
    UsersNotFoundError,
    UserAlreadyExistsError
)


class ErrorMessageUserNotFound(BaseModel):
    detail: str = Field(example=UserNotFoundError.message)


class ErrorMessageUsersNotFound(BaseModel):
    detail: str = Field(example=UsersNotFoundError.message)


class ErrorMessageUserAlreadyExists(BaseModel):
    detail: str = Field(example=UserAlreadyExistsError.message)
