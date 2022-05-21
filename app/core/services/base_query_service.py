from abc import ABC, abstractmethod
from typing import Sequence, TypeVar, Generic

T = TypeVar('T')

class QueryService(ABC, Generic[T]):

    @abstractmethod
    def find_by_id(self, id_: int) -> T | None:
        raise NotImplementedError()

    @abstractmethod
    def findall(self) -> Sequence[T]:
        raise NotImplementedError()
