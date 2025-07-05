import os
from typing import Union, Optional

from src.helpers.functions import ensure_path_exists
from src.types.file_system_directory import FileSystemDirectory
from src.types.file_system_file import FileSystemFile


class ContentLoader:
    def __init__(self, path: str) -> None:
        self.path = path

    def load_content(self, path: Optional[str] = None) -> list[Union[FileSystemDirectory, FileSystemFile]]:
        path = path or self.path
        ensure_path_exists(path=path)

    def _load_content(self, path: Optional[str] = None) -> Union[FileSystemDirectory, FileSystemFile]:
        content = os.list
