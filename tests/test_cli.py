import os
import tempfile
import time
import unittest
from pathlib import Path

from logwash.cli import find_logs, main


def _touch(path, age_days=0):
    path.write_text("x" * 128)
    ts = time.time() - age_days * 86400
    os.utime(path, (ts, ts))


class FindLogsTest(unittest.TestCase):
    def test_age_filter(self):
        with tempfile.TemporaryDirectory() as d:
            old = Path(d) / "old.log"
            new = Path(d) / "new.log"
            _touch(old, age_days=60)
            _touch(new, age_days=1)
            hits = list(find_logs(d, older_than=30))
            self.assertEqual(hits, [old])

    def test_dry_run_keeps_files(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "a.log"
            _touch(f, age_days=90)
            self.assertEqual(main([d, "--older-than", "30", "--dry-run"]), 0)
            self.assertTrue(f.exists())


if __name__ == "__main__":
    unittest.main()
