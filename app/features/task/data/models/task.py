from typing import TypeVar, TYPE_CHECKING

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped

from app.core.models.postgres.models import Base
from app.features.task.domain.entities.task_entity import TaskEntity
from app.features.task.domain.entities.task_query_model import TaskReadModel

if TYPE_CHECKING:
    from app.features.user.data.models.user import User


class Task(Base):
    """
        Task DTO is an object associated with user entity
    """
    __tablename__ = 'tasks'

    title: Mapped[str] | str = Column(String, index=True)
    is_completed: Mapped[bool] | bool | None = Column(Boolean, default=False)
    owner_id: Mapped[int] | int = Column(Integer, ForeignKey('users.id_'))

    owner: Mapped['User'] = relationship('User', back_populates='tasks', uselist=False)

    def to_entity(self) -> TaskEntity:
        return TaskEntity(
            id_=self.id_,
            title=self.title,
            is_deleted=self.is_deleted,
            is_completed=self.is_completed,
            owner_id=self.owner_id,
            updated_at=self.updated_at,
            created_at=self.created_at
        )

    def to_read_model(self) -> TaskReadModel:
        return TaskReadModel(
            id_=self.id_,
            title=self.title,
            is_deleted=self.is_deleted,
            is_completed=self.is_completed,
            owner_id=self.owner_id,
            updated_at=self.updated_at,
            created_at=self.created_at
        )

    def to_dict(self):
        return {
            'id_': self.id_,
            'title': self.title,
            'is_completed': self.is_completed,
            'owner_id': self.owner_id,
            'is_active': self.is_active,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'is_deleted': self.is_deleted,
        }

    @staticmethod
    def from_entity(task: TaskEntity) -> 'Task':
        return Task(
            id_=task.id_,
            title=task.title,
            is_deleted=task.is_deleted,
            is_completed=task.is_completed,
            owner_id=task.owner_id,
            updated_at=task.updated_at,
            created_at=task.created_at
        )
