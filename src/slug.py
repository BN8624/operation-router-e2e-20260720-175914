# 슬러그 정규화 헬퍼
"""Slug normalization helpers."""

import re


def normalize_slug(text: str, max_length: int | None = None) -> str:
    """Lowercase text and normalize whitespace/underscores to single hyphens."""
    text = text.lower()
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    text = text.strip("-")
    if max_length is None:
        return text
    if max_length <= 0:
        return ""
    return text[:max_length].rstrip("-")


def is_valid_slug(text: str) -> bool:
    """Return True if text is lowercase letters/digits/hyphens only and does
    not start or end with a hyphen."""
    if not text:
        return False
    if not re.fullmatch(r"[a-z0-9-]+", text):
        return False
    return not text.startswith("-") and not text.endswith("-")


def slug_prefix(text: str, length: int) -> str:
    """Return the first `length` characters of normalize_slug(text), with any
    trailing hyphen removed."""
    return normalize_slug(text)[:length].rstrip("-")


def slug_from_args(args, max_length=None):
    """Join non-empty args with a single space, then return normalize_slug of the result.

    Items that are None or contain only whitespace (including empty strings)
    are skipped. If no valid items remain, return "".
    """
    valid = [arg for arg in args if arg is not None and arg.strip() != ""]
    if not valid:
        return ""
    return normalize_slug(" ".join(valid), max_length=max_length)
