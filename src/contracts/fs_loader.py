from abc import abstractmethod, ABC
from typing import Self, List

from src.types.annotations import FSItemT


class FileSystemContentLoader(ABC):
    connection_string: str
    path: str

    @abstractmethod
    def connect(self, con: str) -> Self:
        pass

    @abstractmethod
    def list_items(self, path: str) -> List[FSItemT]:
        pass

    @abstractmethod
    def set_path(self, path: str) -> None:
        pass
