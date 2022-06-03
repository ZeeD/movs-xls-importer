from datetime import date
from decimal import Decimal
from typing import Union, cast

from movs.model import Row

from .abc import AWriterPP


def _date(raw: str) -> date:
    dd, mm, yy = raw.split('/', 2)
    return date(int(yy, 10), int(mm, 10), int(dd, 10))


_TWOPLACES = Decimal(10) ** -2


class WriterPPV2(AWriterPP):
    def row(self, raw: list[Union[str, float]]) -> Row:
        data_contabile, data_valuta, importo_raw, descrizione = cast(
            tuple[str, str, float, str], raw)
        importo = Decimal(importo_raw).quantize(_TWOPLACES)
        return Row(data_contabile=_date(data_contabile),
                   data_valuta=_date(data_valuta),
                   addebiti=None if importo > 0 else -importo,
                   accrediti=importo if importo > 0 else None,
                   descrizione_operazioni=descrizione)
