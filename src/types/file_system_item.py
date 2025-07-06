import os

from src.const import FileSystemItemType
from src.helpers.functions import raise_path_doesnot_exist, ensure_path_exists, ensure_is_file


class FileSystemItem:
    path: str
    name: str
    full_path: str
    typ: FileSystemItemType

    def __init__(self, path: str, typ: FileSystemItemType):
        os.path.normpath(path)
        self.typ = typ
        if not os.path.exists(path):
            raise_path_doesnot_exist(path)
        if typ:
            if self.is_anytype:
                ensure_path_exists(path=path)
            elif self.is_file:
                ensure_is_file(path=path)
            elif self.is_dir:
                ensure_path_exists(path=path)
            else:
                raise TypeError(f"FileSystemItem type {typ} is not supported")


        self.full_path = path
        self.path, self.name = os.path.split(path)
        self.typ = typ

    @property
    def is_file(self) -> bool:
        return self.typ == FileSystemItemType.FILE

    @property
    def is_dir(self) -> bool:
        return self.typ == FileSystemItemType.DIR

    @property
    def is_anytype(self) -> bool:
        return self.typ == FileSystemItemType.Any

    def rename(self, new_path: str, force: bool = False) -> str:
        split_path = os.path.split(new_path)

        new_path = os.path.normpath(new_path)

        if not split_path[0]:
            new_path = os.path.join(self.path, split_path[1])
        else:
            ensure_path_exists(path=new_path)

        if force:
            os.replace(self.full_path, new_path)
        else:
            os.rename(self.full_path, new_path)

        self.path, self.name = os.path.split(new_path)

        return new_path

    def __str__(self):
        return f"FileSystemItem<self.typ={self.typ}, path={self.path}, name={self.name}>"
