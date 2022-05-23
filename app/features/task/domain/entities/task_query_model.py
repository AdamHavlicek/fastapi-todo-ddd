from datetime import datetime

from pydantic import Field

from app.features.task.domain.entities.task_common_model import TaskBaseModel
from app.features.task.domain.entities.task_entity import TaskEntity


class TaskReadModel(TaskBaseModel):
    id_: int = Field(example=111)
    is_completed: bool = Field(example=True)
    is_deleted: bool = Field(example=True)
    created_at: datetime
    updated_at: datetime

    class Config(object):
        orm_mode = True

    @classmethod
    def from_entity(cls, entity: TaskEntity) -> 'TaskReadModel':
        return cls(
            id_=entity.id_,
            title=entity.title,
            owner_id=entity.owner_id,
            is_completed=entity.is_completed,
            is_deleted=entity.is_deleted,
            created_at=entity.created_at,
            updated_at=entity.updated_at
        )
