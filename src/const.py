import enum


class FileSystemItemType(enum.StrEnum):
    DIR = enum.auto()
    FILE = enum.auto()
    Any = enum.auto()
