from abc import ABC, abstractmethod
from typing import TypeVar, Sequence, Generic

T = TypeVar('T')


class BaseRepository(ABC, Generic[T]):
    """
        Abstract generic Repository
    """

    @abstractmethod
    def create(self, entity: T) -> T | None:
        raise NotImplementedError()

    @abstractmethod
    def findall(self) -> Sequence[T]:
        raise NotImplementedError()

    @abstractmethod
    def find_by_id(self, id_: int) -> T | None:
        raise NotImplementedError()

    @abstractmethod
    def update(self, entity: T) -> T | None:
        raise NotImplementedError()

    @abstractmethod
    def delete_by_id(self, id_: int) -> T | None:
        raise NotImplementedError()
