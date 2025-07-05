from typing import TypeAlias, Union, Callable, TYPE_CHECKING, Optional, List, Any


if TYPE_CHECKING:
    from src.tools.find import FindParsedSource
    from src.types.file_system_directory import FileSystemDirectory
    from src.types.file_system_file import FileSystemFile



FSItemT: TypeAlias = Union[FileSystemFile, FileSystemDirectory]

FindExecCallback: TypeAlias = Callable[
    [
        FSItemT,
        Optional[
            Union[
                List["FindParsedSource"],
                "FindParsedSource"
            ],
        ],
    ],
    Any
]
