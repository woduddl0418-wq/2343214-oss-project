
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "collect_metrics.py"
OUTPUT = ROOT / "metrics" / "dora-metrics.json"


class TestDoraMetrics(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run(
            [sys.executable, str(SCRIPT)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )

        with OUTPUT.open("r", encoding="utf-8") as f:
            cls.metrics = json.load(f)

    def test_lead_time(self):
        self.assertEqual(
            self.metrics["lead_time_for_changes_hours"], 2.0
        )

    def test_mttr(self):
        self.assertEqual(self.metrics["mttr_hours"], 1.5)

    def test_deployment_count(self):
        self.assertEqual(self.metrics["deployment_count_total"], 1)

    def test_change_failure_rate(self):
        self.assertEqual(
            self.metrics["change_failure_rate_percent"], 100.0
        )

    def test_output_file_exists(self):
        self.assertTrue(OUTPUT.exists())


if __name__ == "__main__":
    unittest.main()

