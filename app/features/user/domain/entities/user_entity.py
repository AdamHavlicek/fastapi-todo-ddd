from datetime import datetime


class UserEntity(object):
    """
     User represents your collection of users as an entity
    """

    def __init__(
        self,
        id_: int,
        email: str,
        password: str,
        is_active: bool | None = True,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
        is_deleted: bool | None = False,
        tasks: list[int] = None
    ):
        self.id_ = id_
        self.email = email
        self.password = password
        self.is_active = is_active
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_deleted = is_deleted
        self.tasks = [tasks, []][tasks is None]

    def __eq__(self, other: object) -> bool:
        if isinstance(other, UserEntity):
            return self.id_ == other.id_

        return False
