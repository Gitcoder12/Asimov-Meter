"""Tests for company mind maps and comparable trend charts."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from visualizations import company_mindmap, compatible_trend_chart, load_company_catalogue

ROOT = Path(__file__).resolve().parents[1]


class VisualizationTests(unittest.TestCase):
    def test_catalogue_is_sourced_and_mindmap_contains_key_organizations(self):
        catalogue = load_company_catalogue(ROOT / "data" / "company_landscape.json")
        diagram = company_mindmap(catalogue)
        self.assertIn("OpenAI", diagram)
        self.assertIn("NVIDIA", diagram)
        self.assertIn("Neuralink", diagram)
        self.assertIn("Gemini Robotics 2.5", diagram)

    def test_trend_chart_uses_one_compatible_group_only(self):
        base = {
            "system": "Example model",
            "sector": "research",
            "indicator": "task_success",
            "unit": "percentage_points",
            "population": "evaluation cohort A",
            "method": "fixed benchmark v1",
        }
        observations = [
            {**base, "period_start": "2026-02-01", "value": 72.0},
            {**base, "period_start": "2026-01-01", "value": 68.0},
        ]
        chart = compatible_trend_chart(observations)
        self.assertIn("xychart-beta", chart)
        self.assertIn('"2026-01-01", "2026-02-01"', chart)
        self.assertIn("68, 72", chart)

    def test_trend_chart_rejects_mixed_units(self):
        first = {
            "system": "Example", "sector": "research", "indicator": "latency",
            "unit": "milliseconds", "population": "same", "method": "same",
            "period_start": "2026-01-01", "value": 100,
        }
        second = {**first, "unit": "seconds", "period_start": "2026-02-01", "value": 0.1}
        with self.assertRaises(ValueError):
            compatible_trend_chart([first, second])

    def test_catalogue_rejects_missing_source_url(self):
        bad = {
            "schema_version": "1.0",
            "companies": [{"company": "Example", "products": [{"name": "Model"}]}],
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "catalogue.json"
            path.write_text(json.dumps(bad), encoding="utf-8")
            with self.assertRaises(ValueError):
                load_company_catalogue(path)


if __name__ == "__main__":
    unittest.main()
