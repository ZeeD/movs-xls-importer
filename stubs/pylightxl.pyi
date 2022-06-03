from typing import BinaryIO, Iterable, Union


class Worksheet:
    rows: Iterable[list[Union[str, float]]]


class Database:
    ws_names: list[str]

    def ws(self, _ws: str) -> Worksheet:
        ...


def readxl(_f: BinaryIO) -> Database:
    ...
