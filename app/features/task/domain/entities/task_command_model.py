from pydantic import Field

from app.features.task.domain.entities.task_common_model import TaskBaseModel


class TaskCreateModel(TaskBaseModel):
    pass


class TaskUpdateModel(TaskBaseModel):
    is_completed: bool = Field(example=True)
    is_deleted: bool = Field(example=True)