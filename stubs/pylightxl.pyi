from typing import BinaryIO, Iterable


class Worksheet:
    rows: Iterable[list[str]]


class Database:
    ws_names: list[str]

    def ws(self, _ws: str) -> Worksheet:
        ...


def readxl(_f: BinaryIO) -> Database:
    ...
