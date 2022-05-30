import copy
from datetime import datetime
from typing import Any, Callable, TYPE_CHECKING

from app.core.error.invalid_operation_exception import InvalidOperationError

if TYPE_CHECKING:
    from app.features.user.domain.entities.user_command_model import UserUpdateModel


class UserEntity(object):
    """
     User represents your collection of users as an entity
    """

    def __init__(
        self,
        id_: int | None,
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
        self.tasks: list[int] = [] if tasks is None else tasks

    def update_entity(
        self,
        entity_update_model: 'UserUpdateModel',
        get_update_data_fn: Callable[['UserUpdateModel'], dict[str, Any]]
    ) -> 'UserEntity':
        update_data = get_update_data_fn(entity_update_model)
        update_entity = copy.deepcopy(self)

        for attr_name, value in update_data.items():
            update_entity.__setattr__(attr_name, value)

        return update_entity

    def mark_entity_as_deleted(self) -> 'UserEntity':
        if self.is_deleted:
            raise InvalidOperationError('User is already marked as deleted')

        marked_entity = copy.deepcopy(self)
        marked_entity.is_deleted = True

        return marked_entity

    def __eq__(self, other: object) -> bool:
        if isinstance(other, UserEntity):
            return self.id_ == other.id_

        return False

    def to_popo(self) -> object:
        return self.__dict__
