from src.builders.file_system_tree_builder import FileSystemTreeBuilder
from src.contracts.fs_loader import FileSystemContentLoader
from src.loaders.local_fs_loader import LocalFSLoader

split_fp = __file__.split("/")

path = "/".join(split_fp[:-1])

content_loader = LocalFSLoader.connect(path)
builder = FileSystemTreeBuilder(path=path, content_loader=content_loader)

cur_dir = builder.build()

for item in cur_dir.list_content():
    print(item)
    if item.is_dir:
        print(item.files)
