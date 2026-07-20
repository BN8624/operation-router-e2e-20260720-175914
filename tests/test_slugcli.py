# 슬러그 CLI 통합 테스트
"""Integration tests for the slug CLI entry point."""

import subprocess
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CLI = REPO_ROOT / "src" / "slugcli.py"


class TestSlugCli(unittest.TestCase):
    def test_cli_prints_normalized_slug(self):
        result = subprocess.run(
            [sys.executable, str(CLI), "Hello", "World"],
            capture_output=True,
            text=True,
            cwd=str(REPO_ROOT),
            check=False,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "hello-world")

    def test_cli_no_args_exits_2(self):
        result = subprocess.run(
            [sys.executable, str(CLI)],
            capture_output=True,
            text=True,
            cwd=str(REPO_ROOT),
            check=False,
        )
        self.assertEqual(result.returncode, 2)
        self.assertTrue(result.stderr.strip())


if __name__ == "__main__":
    unittest.main()
