from typing import BinaryIO, TextIO

from pylightxl import readxl

from .impl.abc import AWriterPP
from .impl.v1 import WriterPPV1
from .impl.v2 import WriterPPV2


def movsxlsimporter(src: BinaryIO, dst: TextIO) -> None:
    db = readxl(src)
    rows = list(db.ws(db.ws_names[0]).rows)
    assert rows[:2] == [
        ['', '', '', ''],
        ['', '', '', '']
    ], rows[:2]

    writer_pp: AWriterPP
    if rows[2] == ['DATA CONTABILE', 'DATA VALUTA', 'IMPORTO', 'DESCRIZIONE']:
        writer_pp = WriterPPV1(dst, rows[3:])
    elif rows[2] == ['Data Contabile', 'Data Valuta', 'Importo (euro)',
                     'Descrizione operazioni']:
        writer_pp = WriterPPV2(dst, rows[3:])
    else:
        raise Exception(rows[3])

    writer_pp.write_pp()
