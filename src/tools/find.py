import os
from typing import Tuple, Any, Generator, Dict, Optional

from src.helpers.functions import parse_extension
from src.types.annotations import FindExecCallback, FSItemT, FindCheckCallback
from src.types.file_system_directory import FileSystemDirectory


class FindParsedSource:
    """
    Class to parse src and make formatted destination.
    The 'Find' destination can be formatted like this:
        {} -> Full path to a selected src file.
        {name} -> Name of the selected dst file.
        {ext} -> Extension of the selected dst file.
        {path} -> Path of the selected dst file (only directory, without name and without slash at the end).
    For example:
        src: "/Users/fakhriddin3040/Development/Projects"

        The parsed data will be:
            name: Projects
            extension: ""
            path: "/Users/fakhriddin3040/Development

        And if there is a destination format has {<placeholder>} without shielding,
        then it will parse it:
            Example:
                dest: {name}.py
                The result will be: Projects.py
    """

    name: str
    extension: str
    path: str # Without end slash

    def __init__(self, src: str, kwargs: Dict[str, str]) -> None:
        self.src = src
        self.path, self.name = os.path.split(src)
        self.extension = parse_extension(self.name)
        self.kwargs = kwargs

    def parse_dest(self, dst: str) -> str:
        return (
            dst.replace("{name}", self.name)
                .replace("{ext}", self.extension)
                .replace("{path}", self.path)
                .replace("{}", self.src)
        )


class Find:
    root: FileSystemDirectory
    current: FileSystemDirectory
    dst: Tuple[str, ...]
    src: str
    use_re: bool
    parsed_source: FindParsedSource

    def __init__(self, *dst, root: FileSystemDirectory, src: str, use_re: bool = False) -> None:
        """
        Rename 'src' to 'dst' recursively.
        Supports regex and dst formatting
        Format like this:
            {} -> Full path to a selected src file.
            {name} -> Name of the selected dst file.
            {ext} -> Extension of the selected dst file.
            {path} -> Path of the selected dst file (only directory, without name and without slash at the end).

            Example:
                copy_recursive('src', '{path}/{name}/.pyx', 'dst', use_re=True)

                Result:
                    All nested files in src with extension '.py' will be copied to into the '.pyx'

        :param root: Root directory to copy from
        :param src: What to find
        :param dst:
        :param use_re:
        :return:
        """
        self.current_path = root
        self.root = root
        self.dst = dst
        self.use_re = use_re
        self.src = src
        self.parsed_source = FindParsedSource(src=src)

        if self.dst:
            self.dst = tuple(
                self.parsed_source.parse_dest(dst) for dst in self.dst
            )

    def find(self, check: FindCheckCallback) -> Generator[FileSystemDirectory, None, None]:
        result = self._find(check=check, item=self.root)
        yield from result

    def _find(self, check: FindCheckCallback, item: FSItemT) -> Generator[FSItemT | None, None, None]:
        if check(item):
            yield item
        if item.is_file:
            return
        elif item.is_dir:
            for itm in item.list_content():
                yield from self._find(check=check, item=itm)
