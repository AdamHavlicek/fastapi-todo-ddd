from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from core.models.postgres.models import Base
from features.task.domain.entities.task_entity import TaskEntity
from features.task.domain.entities.task_query_model import TaskReadModel


class Task(Base):
    """
        Task DTO is an object associated with user entity
    """
    __tablename__ = 'tasks'

    title: Column | str = Column(String, index=True)
    is_completed: Column | bool = Column(Boolean, default=False)
    owner_id: Column | int = Column(Integer, ForeignKey('users.id_'))

    owner = relationship('User', back_populates='tasks')

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

    @staticmethod
    def from_entity(task: TaskEntity) -> 'Task':
        return Task(
            title=task.title,
            is_deleted=task.is_deleted,
            is_completed=task.is_completed,
            owner_id=task.owner_id,
            updated_at=task.updated_at,
            created_at=task.created_at
        )
