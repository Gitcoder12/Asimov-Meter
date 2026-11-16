import tempfile
import unittest
from pathlib import Path

from asimov_meter import Observation, build_report, load_ledger, save_ledger


def observation(**overrides):
    values = dict(
        id="obs-1", system="Example system", sector="education",
        indicator="completion_rate_change", direction="benefit", value=4.2,
        unit="percentage_points", period_start="2025-01-01", period_end="2025-03-31",
        population="One evaluated cohort", method="Pre/post study with stated comparison group",
        source_url="https://example.org/report", verification="reported", notes="",
        recorded_at="2025-04-01T00:00:00+00:00",
    )
    values.update(overrides)
    return Observation.from_dict(values)


class ObservationTests(unittest.TestCase):
    def test_rejects_non_http_source(self):
        with self.assertRaises(ValueError):
            observation(source_url="not-a-url")

    def test_rejects_reversed_period(self):
        with self.assertRaises(ValueError):
            observation(period_start="2025-04-01", period_end="2025-03-31")

    def test_rejects_non_finite_value(self):
        with self.assertRaises(ValueError):
            observation(value=float("nan"))

    def test_report_keeps_units_and_indicators_separate(self):
        report = build_report([
            observation(),
            observation(id="obs-2", value=2.0),
            observation(id="obs-3", indicator="energy_use", unit="kWh", value=8),
        ])
        self.assertEqual(report["observation_count"], 3)
        self.assertEqual(report["group_count"], 2)
        self.assertIn("do not establish causality", report["interpretation"])

    def test_atomic_ledger_round_trip(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "observations.json"
            save_ledger(path, [observation()])
            loaded = load_ledger(path)
            self.assertEqual(loaded[0].id, "obs-1")
            self.assertEqual(loaded[0].value, 4.2)

    def test_report_does_not_pool_different_populations_or_methods(self):
        report = build_report([
            observation(),
            observation(id="obs-2", population="A different cohort"),
            observation(id="obs-3", method="A different study design"),
        ])
        self.assertEqual(report["group_count"], 3)
        self.assertTrue(all("population" in group and "method" in group for group in report["groups"]))

    def test_ledger_rejects_duplicate_ids(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "observations.json"
            save_ledger(path, [observation(), observation()])
            with self.assertRaises(ValueError):
                load_ledger(path)


if __name__ == "__main__":
    unittest.main()
