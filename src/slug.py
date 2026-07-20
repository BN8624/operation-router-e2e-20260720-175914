# 슬러그 정규화 헬퍼
"""Slug normalization helpers."""

import re


def normalize_slug(text: str) -> str:
    """Lowercase text and normalize whitespace/underscores to single hyphens."""
    text = text.lower()
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")
