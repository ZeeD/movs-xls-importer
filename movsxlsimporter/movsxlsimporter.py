from datetime import date
from decimal import Decimal
from typing import BinaryIO, TextIO

from movs import write_csv, write_kv
from movs.model import KV, Row
from pylightxl import readxl

ZERO = Decimal(0)


_MONTHS = ['gen', 'feb', 'mar', 'apr', 'mag', 'giu',
           'lug', 'ago', 'set', 'ott', 'nov', 'dic']


def _date(raw: str) -> date:
    dd, mm, yy = raw.split(' ', 2)
    return date(int(yy, 10), _MONTHS.index(mm) + 1, int(dd, 10))


def _row(raw: list[str]) -> Row:
    data_contabile, data_valuta, importo_raw, descrizione = raw
    importo = Decimal(importo_raw.replace('.', '')
                                 .replace(',', '.')
                                 .removesuffix('\xa0€'))
    return Row(data_contabile=_date(data_contabile),
               data_valuta=_date(data_valuta),
               addebiti=None if importo > 0 else -importo,
               accrediti=importo if importo > 0 else None,
               descrizione_operazioni=descrizione)


def movsxlsimporter(src: BinaryIO, dst: TextIO) -> None:
    write_kv(dst, KV(da=None, a=None, tipo='', conto_bancoposta='',
                     intestato_a='', saldo_al=None, saldo_contabile=ZERO,
                     saldo_disponibile=ZERO))

    db = readxl(src)
    rows = list(db.ws(db.ws_names[0]).rows)
    assert rows[:3] == [
        ['', '', '', ''],
        ['', '', '', ''],
        ['DATA CONTABILE', 'DATA VALUTA', 'IMPORTO', 'DESCRIZIONE']
    ]

    write_csv(dst, (_row(row) for row in rows[3:]))
