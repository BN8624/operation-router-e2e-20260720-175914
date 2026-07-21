# 슬러그 정규화 단위 테스트
"""Unit tests for normalize_slug."""

import unittest

from src.slug import is_valid_slug, normalize_slug, slug_from_args, slug_prefix


class TestNormalizeSlug(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(normalize_slug("Hello World"), "hello-world")

    def test_whitespace_and_underscores(self):
        self.assertEqual(normalize_slug("  a__b   c  "), "a-b-c")

    def test_only_hyphens(self):
        self.assertEqual(normalize_slug("---"), "")

    def test_without_max_length_preserves_existing_behavior(self):
        self.assertEqual(normalize_slug("  Hello__World  "), "hello-world")

    def test_max_length_truncates_normalized_slug(self):
        self.assertEqual(normalize_slug("hello world", max_length=8), "hello-wo")

    def test_max_length_strips_trailing_hyphen(self):
        self.assertEqual(normalize_slug("hello world", max_length=6), "hello")


class TestSlugFromArgs(unittest.TestCase):
    def test_slug_from_args_hello_world(self):
        self.assertEqual(slug_from_args(["Hello", "World"]), "hello-world")

    def test_slug_from_args_max_length(self):
        self.assertEqual(slug_from_args(["Hello", "World"], max_length=6), "hello")

    def test_slug_from_args_skips_none_and_blank_entries(self):
        self.assertEqual(
            slug_from_args(["Hello", None, "", "  ", "World"]), "hello-world"
        )

    def test_slug_from_args_all_invalid_returns_empty_string(self):
        self.assertEqual(slug_from_args([None, "", "   "]), "")


class TestSlugPrefix(unittest.TestCase):
    def test_slug_prefix_truncates_normalized_slug(self):
        self.assertEqual(slug_prefix("Hello World", 5), "hello")

    def test_slug_prefix_strips_trailing_hyphen(self):
        self.assertEqual(slug_prefix("Hello World", 6), "hello")


class TestIsValidSlug(unittest.TestCase):
    def test_is_valid_slug_accepts_valid_case(self):
        self.assertTrue(is_valid_slug("hello-world-123"))

    def test_is_valid_slug_rejects_leading_hyphen(self):
        self.assertFalse(is_valid_slug("-hello-world"))


if __name__ == "__main__":
    unittest.main()
