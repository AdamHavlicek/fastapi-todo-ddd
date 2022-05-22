from datetime import datetime


class TaskEntity(object):
    """
        Task represents your collection of tasks as an entity
    """

    def __init__(
        self,
        id_: int,
        title: str,
        owner_id: int,
        is_completed: bool | None = False,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
        is_deleted: bool | None = False,
    ):
        self.id_ = id_
        self.title = title
        self.is_completed = is_completed
        self.owner_id = owner_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_deleted = is_deleted

    def __eq__(self, other) -> bool:
        if isinstance(other, TaskEntity):
            return self.id_ == other.id_

        return False
