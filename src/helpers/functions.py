import os
from typing import Optional


def raise_path_doesnot_exist(path: str):
    raise FileNotFoundError(f"Path '{path}' does not exist")


def raise_not_a_dir(path: str):
    raise FileNotFoundError(f"Path '{path}' is not a directory")


def raise_not_a_file(path: str):
    raise FileNotFoundError(f"Path '{path}' is not a file")


def ensure_is_directory(path: str):
    if not os.path.isdir(path):
        raise_path_doesnot_exist(path=path)


def ensure_path_exists(path: str):
    if not os.path.exists(path):
        raise_path_doesnot_exist(path=path)


def ensure_is_file(path: str):
    if not os.path.isfile(path):
        raise_not_a_file(path=path)


def is_relative_path(path: str):
    return not path.startswith("/")

def is_absolute_path(path: str):
    return not is_relative_path(path=path)


def parse_extension(path: str) -> str:
    return os.path.splitext(path)[1]
