import os
from typing import Self

from src.contracts.fs_loader import FileSystemContentLoader
from src.helpers.functions import ensure_path_exists
from src.types.file_system_directory import FileSystemDirectory


class FileSystemTreeBuilder:
    _load_content: bool = False
    recursive_load: bool = False

    def __init__(self, path: str, content_loader: FileSystemContentLoader) -> None:
        ensure_path_exists(path=path)
        if not os.path.isdir(path):
            raise TypeError(f"root '{path}' must be a directory.")
        self.path = path
        self.root = FileSystemDirectory(path=path, content_loader=content_loader)
        self.content_loader = content_loader

    def set_path(self, path: str) -> Self:
        self.path = path
        return self

    def build(self) -> FileSystemDirectory:
        return FileSystemDirectory(
            self.path,
            load_content=True,
            content_loader=self.content_loader
        )
