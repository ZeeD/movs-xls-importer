from sys import argv, stdout

from .movsxlsimporter import movsxlsimporter


def main() -> None:
    src_fn = argv[1]
    dst_fn = argv[2] if 2 < len(argv) else '-'

    with open(src_fn, 'rb') as src:
        if dst_fn == '-':
            movsxlsimporter(src, stdout)
        else:
            with open(dst_fn, 'w', encoding='UTF-8') as dst:
                movsxlsimporter(src, dst)
