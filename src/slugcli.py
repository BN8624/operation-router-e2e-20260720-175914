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
    if not args:
        print("usage: python src/slugcli.py <text...>", file=sys.stderr)
        return 2
    print(normalize_slug(" ".join(args)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
