import os
from typing import TYPE_CHECKING, List, Self

from src.contracts.fs_loader import FileSystemContentLoader
from src.types.annotations import FSItemT
from src.types.file_system_directory import FileSystemDirectory
from src.types.file_system_file import FileSystemFile



class LocalFSLoader(FileSystemContentLoader):

    @classmethod
    def connect(cls, con: str) -> Self:
        self = cls()
        return self

    def set_path(self, path: str) -> None:
        self.path = path

    def list_items(self, path: str) -> List[FSItemT]:
        items = os.scandir(path)
        return list(
            FileSystemFile(item.path)
            if item.is_file()
            else FileSystemDirectory(path=item.path, content_loader=self)
            for item in items
        )
