import copy
import json
import unittest
from pathlib import Path

from scripts.validate_record import load_schema, validate_record

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures"


def load_fixture(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


class ValidationTests(unittest.TestCase):
    def test_load_creator_schema(self):
        schema = load_schema("creator")
        self.assertEqual(schema["$id"], "https://ugc.local/schemas/creator.schema.json")

    def test_valid_creator_passes(self):
        self.assertEqual(validate_record("creator", load_fixture("valid-creator.json")), [])

    def test_valid_campaign_passes(self):
        errors = validate_record("campaign", load_fixture("valid-campaign.json"), as_of="2026-08-14")
        self.assertEqual(errors, [])

    def test_valid_performance_passes(self):
        self.assertEqual(validate_record("performance", load_fixture("valid-performance.json")), [])

    def test_valid_scorecard_passes(self):
        self.assertEqual(validate_record("scorecard", load_fixture("valid-scorecard.json")), [])

    def test_paid_deployment_requires_paid_media_rights(self):
        payload = copy.deepcopy(load_fixture("valid-campaign.json"))
        payload["rights"]["paid_media"] = "not_approved"
        errors = validate_record("campaign", payload, as_of="2026-08-14")
        self.assertTrue(any("paid deployment requires rights.paid_media = approved" in error for error in errors))

    def test_paid_deployment_requires_final_approval(self):
        payload = copy.deepcopy(load_fixture("valid-campaign.json"))
        payload["approvals"]["final"] = "pending"
        errors = validate_record("campaign", payload, as_of="2026-08-14")
        self.assertTrue(any("approvals.final = approved" in error for error in errors))

    def test_campaign_blocks_reversed_rights_dates(self):
        payload = copy.deepcopy(load_fixture("valid-campaign.json"))
        payload["rights"]["start_date"] = "2026-11-14"
        payload["rights"]["end_date"] = "2026-08-14"
        errors = validate_record("campaign", payload, as_of="2026-08-14")
        self.assertTrue(any("must not be before" in error for error in errors))

    def test_campaign_blocks_expired_paid_media_rights(self):
        payload = copy.deepcopy(load_fixture("valid-campaign.json"))
        errors = validate_record("campaign", payload, as_of="2026-12-01")
        self.assertTrue(any("paid-media rights are expired" in error for error in errors))

    def test_creator_rejects_unknown_evidence_state(self):
        payload = copy.deepcopy(load_fixture("valid-creator.json"))
        payload["evidence"][0]["state"] = "self_verified"
        errors = validate_record("creator", payload)
        self.assertTrue(any("state" in error and "self_verified" in error for error in errors))

    def test_unknown_performance_metric_must_be_null_not_zero(self):
        payload = copy.deepcopy(load_fixture("valid-performance.json"))
        payload["metrics"]["leads"] = 0
        errors = validate_record("performance", payload)
        self.assertTrue(any("unknown metric leads must be null" in error for error in errors))

    def test_scorecard_rejects_undefined_decision(self):
        payload = copy.deepcopy(load_fixture("valid-scorecard.json"))
        payload["decision"] = "maybe_renew"
        errors = validate_record("scorecard", payload)
        self.assertTrue(any("decision" in error for error in errors))

    def test_reference_metadata_requires_reference_only_true(self):
        self.assertTrue(validate_record("reference", {"reference_only": False}))
        self.assertEqual(validate_record("reference", {"reference_only": True}), [])

    def test_reference_readme_contains_required_guard(self):
        text = (ROOT / "examples" / "media-kits" / "README.md").read_text(encoding="utf-8").lower()
        self.assertIn("reference_only: true", text)
        self.assertIn("does not define ugc operating standards or scoring rules", text)

    def test_reference_pdf_hash_matches_repository_reference(self):
        from hashlib import sha256
        path = ROOT / "examples" / "media-kits" / "creator-paid-pitch-example-kristina-elise.pdf"
        digest = sha256(path.read_bytes()).hexdigest()
        self.assertEqual(digest, "d6aadca9d1fa76fdac8807e7c97842e35670325a2aa0e163e1161543c1c0a4f4")


if __name__ == "__main__":
    unittest.main()
