import os.path

from src.const import FileSystemItemType
from src.helpers.functions import raise_path_doesnot_exist, parse_extension
from src.types.file_system_item import FileSystemItem


class FileSystemFile(FileSystemItem):
    ext: str

    def __init__(self, path):
        if not os.path.isfile(path):
            raise_path_doesnot_exist(path=path)
        super().__init__(path=path, typ=FileSystemItemType.FILE)
        self.ext = parse_extension(path=path)

    def rename(self, new_path: str, force: bool = False) -> str:
        super().rename(new_path=new_path, force=force)
        self.ext = parse_extension(path=new_path)
        return new_path
