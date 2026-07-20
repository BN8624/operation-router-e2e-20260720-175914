# 슬러그 CLI 진입점
"""CLI entry point that prints normalize_slug of joined arguments."""

import sys
from pathlib import Path

# Ensure repo root is importable when run as `python src/slugcli.py`
_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from src.slug import normalize_slug


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    max_length = None
    text_args = []
    index = 0
    while index < len(args):
        argument = args[index]
        if argument == "--max-length":
            if index + 1 == len(args):
                print("usage: python src/slugcli.py [--max-length N] <text...>", file=sys.stderr)
                return 2
            try:
                max_length = int(args[index + 1])
            except ValueError:
                print("usage: python src/slugcli.py [--max-length N] <text...>", file=sys.stderr)
                return 2
            index += 2
            continue
        text_args.append(argument)
        index += 1

    if not text_args:
        print("usage: python src/slugcli.py <text...>", file=sys.stderr)
        return 2
    print(normalize_slug(" ".join(text_args), max_length=max_length))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
