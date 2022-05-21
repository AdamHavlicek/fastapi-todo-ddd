from abc import ABC, abstractmethod
from typing import Sequence

from app.features.user.domain.usecases.user_query_model import UserReadModel


class UserQueryService(ABC):

    @abstractmethod
    def find_by_id(self, id_: int) -> UserReadModel | None:
        raise NotImplementedError()

    @abstractmethod
    def findall(self) -> Sequence[UserReadModel]:
        raise NotImplementedError()
