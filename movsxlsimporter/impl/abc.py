from abc import ABC, abstractmethod
from decimal import Decimal
from typing import TextIO, Union

from movs import write_csv, write_kv
from movs.model import KV, Row

ZERO = Decimal(0)


class AWriterPP(ABC):
    def __init__(self,
                 dst: TextIO,
                 rows: list[list[Union[str, float]]]) -> None:
        self.dst = dst
        self.rows = rows

    def write_pp(self) -> None:
        write_kv(self.dst, KV(da=None, a=None, tipo='', conto_bancoposta='',
                              intestato_a='', saldo_al=None,
                              saldo_contabile=ZERO, saldo_disponibile=ZERO))
        write_csv(self.dst, (self.row(row) for row in self.rows))

    @abstractmethod
    def row(self, _raw: list[Union[str, float]]) -> Row:
        ...
