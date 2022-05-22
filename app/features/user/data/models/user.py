from sqlalchemy import Column, Boolean, String
from sqlalchemy.orm import relationship

from app.features.user.domain.entities.user_query_model import UserReadModel
from core.models.postgres.models import Base
from app.features.user.domain.entities.user_entity import UserEntity


class User(Base):
    """
        User DTO is an object associated with user entity
    """
    __tablename__ = 'users'

    email: str | Column = Column(String, unique=True, index=True)
    password: str | Column = Column(String)
    is_active: bool | Column = Column(Boolean, default=True)

    tasks = relationship('Task', back_populates='owner')

    def to_entity(self) -> UserEntity:
        return UserEntity(
            id_=self.id_,
            email=self.email,
            password=self.password,
            is_active=self.is_active,
            created_at=self.created_at,
            updated_at=self.updated_at,
            is_deleted=self.is_deleted,
            tasks=[task.id_ for task in self.tasks]
        )

    def to_read_model(self) -> UserReadModel:
        return UserReadModel(
            id_=self.id_,
            email=self.email,
            password=self.password,
            is_active=self.is_active,
            is_deleted=self.is_deleted,
            created_at=self.created_at,
            updated_at=self.updated_at,
            tasks=[task.id_ for task in self.tasks]
        )

    @staticmethod
    def from_entity(user: UserEntity) -> 'User':
        return User(
            email=user.email,
            password=user.password,
            is_active=user.is_active,
            created_at=user.created_at,
            updated_at=user.updated_at,
            is_deleted=user.is_deleted
        )
