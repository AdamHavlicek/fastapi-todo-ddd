from datetime import datetime

from pydantic import Field

from app.features.user.domain.entities.user_entity import UserEntity
from app.features.user.domain.entities.user_common_model import UserBaseModel


class UserReadModel(UserBaseModel):
    """
        UserReadModel represents data structure as a read model
    """

    id_: int = Field(example=1111)
    email: str = Field(example='test@test.com')
    password: str = Field(example='password')
    is_active: bool = Field(example=True)
    is_deleted: bool = Field(example=True)
    created_at: datetime
    updated_at: datetime
    tasks: list[int]

    class Config:
        orm_mode = True

    @staticmethod
    def from_entity(entity: UserEntity) -> 'UserReadModel':
        return UserReadModel(
            id_=entity.id_,
            email=entity.email,
            password=entity.password,
            is_active=entity.is_active,
            is_deleted=entity.is_deleted,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
            tasks=entity.tasks
        )
