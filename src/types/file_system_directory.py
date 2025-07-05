import os
from itertools import chain
from typing import TYPE_CHECKING, Optional, Self, Iterable, List, Tuple

from src.helpers.functions import raise_path_doesnot_exist
from src.types.annotations import FSItemT
from src.types.file_system_file import FileSystemFile
from src.types.file_system_item import FileSystemItem
from src.utils.fs_helper import FSHelper

if TYPE_CHECKING:
    from src.const import FileSystemItemType


class FileSystemDirectory(FileSystemItem):
    files: list["FileSystemFile"]
    directories: list["FileSystemDirectory"]

    def __init__(
        self,
        path,
        files: Optional[List["FileSystemFile"]] = None,
        directories: Optional[List["FileSystemDirectory"]] = None,
        load_content: bool = False
    ) -> None:
        """
        File system representation object.
        Can imagine that it is a file system tree's node.
        Has files, directories and loading and refreshing content.
        Also, implemented items lazy loading.
        :param path: The path of directory
        :param files: Optional list of loaded files
        :param directories: Optional list of loaded directories
        :param load_content: Optional flag to load content
        """
        if not os.path.isdir(path):
            raise_path_doesnot_exist(path=path)
        super().__init__(path, typ=FileSystemItemType.DIR)

        self._content_loaded = False

        if load_content:
            self.load_content(path=path)
        else:
            self.files = files or list()
            self.directories = directories or list()

    @classmethod
    def from_items(
        cls, path: str, items: Iterable[FSItemT]
    ) -> "FileSystemDirectory":
        files = [
            item for item in items
            if item.is_file
        ]
        dirs = [
            item for item in items
            if item.is_dir
        ]
        return cls(path=path, files=files, directories=dirs)

    @classmethod
    def from_path(cls, path: str) -> "FileSystemDirectory":
        items = FSHelper.list_items(path=path)
        return cls.from_items(path=path, items=items)

    def get_content(self, path: str) -> Tuple[List["FileSystemDirectory"], List["FileSystemFile"]]:
        items = FSHelper.list_items(path=path)
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
        self._content_loaded = True

    def list_content(self) -> List[FSItemT]:
        if not self._content_loaded:
            self.load_content()

        return list(chain(self.files, self.directories)) # noqa
