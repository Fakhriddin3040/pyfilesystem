from __future__ import annotations


from typing import TypeAlias, Union, Callable, TYPE_CHECKING, Optional, List



if TYPE_CHECKING:
    from src.tools.find import FindParsedSource
    from src.types.file_system_directory import FileSystemDirectory
    from src.types.file_system_file import FileSystemFile


FSItemT: TypeAlias = Union["FileSystemFile", "FileSystemDirectory"]

FindCheckCallback = Callable[[FSItemT], bool]

FindExecCallback: TypeAlias = Callable[
    [
        Optional[Union[List["FSItemT"], "FSItemT"]],
        Optional[Union[List["FindParsedSource"], "FindParsedSource"]],
    ],
    bool
]
