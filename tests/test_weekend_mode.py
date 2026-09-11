from __future__ import annotations

import hashlib
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import weekend_mode  # noqa: E402


class AerospaceGradeLeisureCertification(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.spec = weekend_mode.load_spec()
        cls.protocol_text = weekend_mode.PROTOCOL_PATH.read_text(encoding="utf-8")

    def test_temporal_boundary_ledger_closes_at_exactly_2026(self) -> None:
        result = weekend_mode.run_alignment_evals(self.spec, self.protocol_text)
        self.assertEqual(result["evaluation_count"], 2026)
        self.assertEqual(sum(result["control_hits"].values()), 2026)

    def test_every_control_receives_nearly_equal_aerospace_attention(self) -> None:
        hits = weekend_mode.run_alignment_evals(self.spec, self.protocol_text)["control_hits"]
        self.assertLessEqual(max(hits.values()) - min(hits.values()), 1)

    def test_simulation_spans_25_calendar_years(self) -> None:
        result = weekend_mode.run_friday_simulation(self.spec)
        self.assertEqual(result["calendar_years"], 25)
        self.assertEqual(len(result["annual_friday_ledger"]), 25)

    def test_every_simulated_friday_is_temporally_a_friday(self) -> None:
        friday_dates = weekend_mode.fridays(self.spec)
        self.assertTrue(friday_dates)
        self.assertTrue(all(day.weekday() == 4 for day in friday_dates))

    def test_simulation_creates_no_saturday_scrums(self) -> None:
        result = weekend_mode.run_friday_simulation(self.spec)
        self.assertEqual(result["saturday_scrums_created"], 0)

    def test_only_urgent_or_authorized_scenarios_may_interrupt_brunch(self) -> None:
        allowed = {"urgent", "authorized"}
        for scenario in self.spec["scenarios"]:
            if scenario["brunch_interruptions_allowed"]:
                self.assertIn(scenario["classification"], allowed)

    def test_generated_protocol_matches_controlled_sources(self) -> None:
        self.assertEqual(self.protocol_text, weekend_mode.render_protocol(self.spec))

    def test_committed_evidence_matches_a_fresh_certification(self) -> None:
        expected = weekend_mode.evidence_text(self.spec, self.protocol_text)
        actual = weekend_mode.EVIDENCE_PATH.read_text(encoding="utf-8")
        self.assertEqual(actual, expected)

    def test_committed_soak_report_matches_a_fresh_simulation(self) -> None:
        expected = weekend_mode.friday_report_text(self.spec)
        actual = weekend_mode.FRIDAY_REPORT_PATH.read_text(encoding="utf-8")
        self.assertEqual(actual, expected)

    def test_protocol_digest_is_cryptographically_overqualified(self) -> None:
        evidence = json.loads(weekend_mode.EVIDENCE_PATH.read_text(encoding="utf-8"))
        expected = hashlib.sha256(self.protocol_text.encode("utf-8")).hexdigest()
        self.assertEqual(evidence["protocol"]["sha256"], expected)

    def test_physical_grass_is_not_fraudulently_included(self) -> None:
        evidence = weekend_mode.evidence(self.spec, self.protocol_text)
        self.assertFalse(evidence["attestations"]["physical_grass_included"])


if __name__ == "__main__":
    unittest.main()
