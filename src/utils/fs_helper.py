import os
import shutil
from typing import List

from src.const import FileSystemItemType
from src.types.annotations import FSItemT


class FSHelper:
    @staticmethod
    def rename_with_copy(src: str, dst: str) -> None:
        shutil.copyfile(src, dst)

    @staticmethod
    def rename(src: str, dst: str) -> None:
        shutil.move(src, dst)

    @staticmethod
    def list_items(path: str) -> List[FSItemT]:
        from src.types.file_system_directory import FileSystemDirectory
        from src.types.file_system_file import FileSystemFile

        items = os.scandir(path)
        return list(
            FileSystemFile(path=path)
            if item.is_dir()
            else FileSystemDirectory(path=path)
            for item in items
        )
