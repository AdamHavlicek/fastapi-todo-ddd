from abc import ABC, abstractmethod
from typing import Any


class BaseUseCase(ABC):

    @abstractmethod
    def __call__(self, *args: Any) -> Any:
        raise NotImplementedError()
