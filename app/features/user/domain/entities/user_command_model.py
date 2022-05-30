from pydantic import Field, BaseModel

from app.features.user.domain.entities.user_common_model import UserBaseModel


class UserCreateModel(UserBaseModel):
    """
        UserCreateModel represents a write model to create a user
    """
    password: str = Field(example='password')


class UserUpdateModel(BaseModel):
    """
        UserUpdateModel represents a write model to update a user
    """

    email: str | None
    password: str | None = Field(example='password')
    is_active: bool | None = Field(example=True)
    is_deleted: bool | None = Field(example=True)
