import os.path

from src.const import FileSystemItemType
from src.helpers.functions import raise_path_doesnot_exist, parse_extension, raise_not_a_file
from src.types.file_system_item import FileSystemItem


class FileSystemFile(FileSystemItem):
    ext: str

    def __init__(self, path):
        super().__init__(path=path, typ=FileSystemItemType.FILE)
        self.ext = parse_extension(path=path)

    def rename(self, new_path: str, force: bool = False) -> str:
        super().rename(new_path=new_path, force=force)
        self.ext = parse_extension(path=new_path)
        return new_path

    def __str__(self):
        return (
            "File: \n"
            f"   Path: {self.path}\n"
            f"   Name: {self.name}\n"
            f"   Extension: {self.ext}\n"
        )
