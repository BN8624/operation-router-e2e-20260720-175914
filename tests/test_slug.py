# 슬러그 정규화 단위 테스트
"""Unit tests for normalize_slug."""

import unittest

from src.slug import normalize_slug


class TestNormalizeSlug(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(normalize_slug("Hello World"), "hello-world")

    def test_whitespace_and_underscores(self):
        self.assertEqual(normalize_slug("  a__b   c  "), "a-b-c")

    def test_only_hyphens(self):
        self.assertEqual(normalize_slug("---"), "")


if __name__ == "__main__":
    unittest.main()
