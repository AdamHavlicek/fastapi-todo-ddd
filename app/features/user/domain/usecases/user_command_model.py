from pydantic import Field

from app.features.user.domain.usecases.user_common_model import UserBaseModel


class UserCreateModel(UserBaseModel):
    """
        UserCreateModel represents a write model to create a user
    """
    password: str = Field(example='password')


class UserUpdateModel(UserBaseModel):
    """
        UserUpdateModel represents a write model to update a user
    """

    password: str = Field(example='password')
    is_active: bool = Field(example=True)
    is_deleted: bool = Field(example=True)
