import os
from itertools import chain
from typing import TYPE_CHECKING, Optional, Self, List, Tuple

from src.helpers.functions import raise_path_doesnot_exist
from src.types.file_system_file import FileSystemFile
from src.types.file_system_item import FileSystemItem
from src.const import FileSystemItemType

if TYPE_CHECKING:
    from src.contracts.fs_loader import FileSystemContentLoader
    from src.types.annotations import FSItemT

class FileSystemDirectory(FileSystemItem):
    files: list["FileSystemFile"]
    directories: list["FileSystemDirectory"]

    def __init__(
        self,
        path,
        content_loader: "FileSystemContentLoader",
        load_content: bool = True
    ) -> None:
        """
        File system representation object.
        Can imagine that it is a file system tree's node.
        Has files, directories and loading and refreshing content.
        Also, implemented items lazy loading.
        :param path: The path of directory
        :param load_content: Optional flag to load content
        """
        if not os.path.isdir(path):
            raise_path_doesnot_exist(path=path)
        super().__init__(path, typ=FileSystemItemType.DIR)
        self.content_loaded = False

        self._content_loader = content_loader

        if load_content:
            self.load_content(path=path)

    def get_content(self, path: str) -> Tuple[List["FileSystemDirectory"], List["FileSystemFile"]]:
        items = self._content_loader.list_items(path=path)
        files = [
            item for item in items
            if item.is_file
        ]
        dirs = [
            item for item in items
            if item.is_dir
        ]
        return files, dirs

    def load_content(self, path: Optional[str] = None) -> Self:
        path = path or self.path

        dirs, files = self.get_content(path=path)

        self.files = files
        self.directories = dirs
        self.content_loaded = True

    def refresh_content(self, path: Optional[str] = None) -> Self:
        path = path or self.path
        self.path = path
        self.load_content(path=path)

    def list_content(self) -> List["FSItemT"]:
        if not self._content_loader:
            self.load_content()

        return list(chain(self.files, self.directories)) # noqa

    def __str__(self):
        return (
            "Directory: \n"
            f"   Path: {self.path}\n"
            f"   Name: {self.name}\n"
        )
