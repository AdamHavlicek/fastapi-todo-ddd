from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')


class AbstractUnitOfWork(ABC, Generic[T]):

    repository: T

    @abstractmethod
    def begin(self):
        raise NotImplementedError()

    @abstractmethod
    def commit(self):
        raise NotImplementedError()

    @abstractmethod
    def rollback(self):
        raise NotImplementedError()