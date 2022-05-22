from abc import abstractmethod
from typing import Sequence

from core.repositories.base_repository import BaseRepository
from features.task.domain.entities.task_entity import TaskEntity


class TaskRepository(BaseRepository[TaskEntity]):

    @abstractmethod
    def find_by_owner_id(self, owner_id: int) -> Sequence[TaskEntity]:
        raise NotImplementedError()