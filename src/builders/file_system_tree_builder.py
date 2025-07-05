import os
from typing import Self

from src.helpers.functions import ensure_path_exists
from src.types.file_system_directory import FileSystemDirectory
from src.types.file_system_file import FileSystemFile


class FileSystemTreeBuilder:
    _load_content: bool = False
    recursive_load: bool = False

    def __init__(self, root: str) -> None:
        ensure_path_exists(path=root)
        if not os.path.isdir(root):
            raise TypeError(f"root '{root}' must be a directory.")
        self.path = root

    def set_path(self, path: str) -> Self:
        self.path = path
        return self

    def load_content(self, recursive: bool = True) -> Self:
        self._load_content = True
        self.recursive_load = recursive
        return self

    def dont_load_content(self) -> Self:
        self._load_content = False
        return self

    def refresh_content(self) -> Self:
        return self

    def build(self) -> FileSystemDirectory:
        if not self._load_content:
            :w
