import shutil


class FSHelper:
    @staticmethod
    def rename_with_copy(src: str, dst: str) -> None:
        shutil.copyfile(src, dst)

    @staticmethod
    def rename(src: str, dst: str) -> None:
        shutil.move(src, dst)
