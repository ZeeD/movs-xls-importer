from datetime import date
from decimal import Decimal
from typing import Union, cast

from movs.model import Row

from .abc import AWriterPP

_MONTHS = ['gen', 'feb', 'mar', 'apr', 'mag', 'giu',
           'lug', 'ago', 'set', 'ott', 'nov', 'dic']


def _date(raw: str) -> date:
    dd, mm, yy = raw.split(' ', 2)
    return date(int(yy, 10), _MONTHS.index(mm) + 1, int(dd, 10))


class WriterPPV1(AWriterPP):
    def row(self, raw: list[Union[str, float]]) -> Row:
        data_contabile, data_valuta, importo_raw, descrizione = cast(
            tuple[str, str, str, str], raw)
        importo = Decimal(importo_raw.replace('.', '')
                                     .replace(',', '.')
                                     .removesuffix('\xa0€'))
        return Row(data_contabile=_date(data_contabile),
                   data_valuta=_date(data_valuta),
                   addebiti=None if importo > 0 else -importo,
                   accrediti=importo if importo > 0 else None,
                   descrizione_operazioni=descrizione)
