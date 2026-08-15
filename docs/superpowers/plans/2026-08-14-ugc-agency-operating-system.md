# UGC Agency Operating System Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the UGC repository into the agency-facing source of truth for creator discovery, qualification, outreach, campaign operations, rights, approvals, measurement, scorecards, and renewal decisions.

**Architecture:** Use a skill-first design. `SKILL.md` defines the reusable operating behavior, Markdown files define human-readable workflows and templates, JSON Schema files define structured records, and a small Python validator enforces cross-field business rules that JSON Schema alone does not cover. The future dedicated UGC agent consumes these same files rather than duplicating them.

**Tech Stack:** Markdown, JSON Schema Draft 2020-12, Python 3.11+, `jsonschema` 4.x, Python `unittest`, GitHub repository files.

## Global Constraints

- The repository is the agency-facing source of truth for UGC operations.
- Version 1 covers the full workflow from creator discovery through reporting and renewal decisions.
- The Kristina Elise media kit is reference-only and must not define, train, score, rank, or control the UGC skill.
- No scoring rule, qualification threshold, payment recommendation, campaign standard, or workflow requirement may be derived from the Kristina example alone.
- Creator-provided claims remain creator-provided until independently verified.
- Missing performance metrics remain unknown and must never be estimated.
- Organic rights, brand usage rights, paid media rights, and whitelisting or partnership-ad permissions are distinct states.
- Publishing or paid deployment is blocked until required approvals and rights are present.
- Existing responsibilities of Content Scaling, Creative Operating System, AI Video, Adley, and Otto are referenced, not duplicated.
- Version 1 does not build a separate UGC agent runtime or memory system.

---

## File Structure

### Root operating files
- `README.md`: repository purpose, workflow, read order, boundaries, and validation commands.
- `AGENTS.md`: rules for agents reading or changing this repository.
- `SKILL.md`: reusable UGC operating skill used by approved agents.
- `TASKS.md`: version 1 completion checklist and future agent-runtime backlog.
- `requirements-dev.txt`: pinned development dependency range for JSON Schema validation.

### Workflow documentation
- `docs/creator-discovery.md`: discovery evidence, source quality, fact states, qualification process.
- `docs/creator-outreach.md`: outreach sequence, response tracking, negotiation handoff.
- `docs/campaign-workflow.md`: stage-by-stage campaign operating flow.
- `docs/rights-and-usage.md`: rights states, dates, disclosures, conflicts, and deployment gates.
- `docs/measurement.md`: objective-specific metrics and scorecard interpretation.

### Reusable templates
- `templates/creator-profile.md`
- `templates/creator-scorecard.md`
- `templates/outreach-message.md`
- `templates/ugc-campaign-brief.md`
- `templates/script-brief.md`
- `templates/rights-agreement-checklist.md`
- `templates/media-kit-template.md`

### Structured contracts
- `schemas/creator.schema.json`
- `schemas/campaign.schema.json`
- `schemas/performance.schema.json`
- `schemas/scorecard.schema.json`

### Validation
- `scripts/validate_record.py`: schema validation plus UGC-specific cross-field rules.
- `tests/test_validate_record.py`: creator, campaign, performance, scorecard, and reference-metadata tests.
- `tests/fixtures/valid-creator.json`
- `tests/fixtures/valid-campaign.json`
- `tests/fixtures/valid-performance.json`
- `tests/fixtures/valid-scorecard.json`

### Reference example and future agent boundary
- `examples/media-kits/README.md`: reference-only policy and provenance metadata.
- `examples/media-kits/creator-paid-pitch-example-kristina-elise.pdf`: uploaded source file, unchanged.
- `agent/README.md`: future dedicated agent boundary and activation criteria.

---

### Task 1: Repository shell and operating boundaries

**Files:**
- Create: `README.md`
- Create: `AGENTS.md`
- Create: `TASKS.md`
- Create: `requirements-dev.txt`
- Create: `agent/README.md`

**Interfaces:**
- Consumes: approved design at `docs/superpowers/specs/2026-08-14-ugc-agency-operating-system-design.md`.
- Produces: repository-wide ownership rules and the read order used by all later tasks.

- [ ] **Step 1: Write the root README**

Include this read order and workflow verbatim in structure:

```markdown
## Read Order
1. `AGENTS.md`
2. `SKILL.md`
3. `docs/campaign-workflow.md`
4. `docs/rights-and-usage.md`
5. `docs/measurement.md`
6. `schemas/`
7. `templates/`

## Version 1 Workflow
Creator discovery -> qualification -> outreach -> response tracking -> selection -> campaign brief -> hooks/scripts -> rates/payment -> rights -> delivery -> QA/approval -> deployment handoff -> performance -> scorecard -> renew/retest/pause/retire.
```

State that UGC owns creator-specific operating rules while Content Scaling, Creative Operating System, AI Video, Adley, and Otto retain their existing specialist responsibilities.

- [ ] **Step 2: Write `AGENTS.md`**

Require these rules:

```markdown
- Do not invent creator metrics, rights, rates, approvals, or verification status.
- Preserve `creator_provided`, `agency_observed`, `verified`, and `unknown` as distinct evidence states.
- Never infer paid-media rights from organic posting rights.
- Never deploy content with expired or missing required rights.
- Never use files under `examples/` as scoring standards.
- Route specialist work to the owning repository instead of copying its logic here.
```

- [ ] **Step 3: Write `TASKS.md` and `agent/README.md`**

`TASKS.md` must mark the skill-first operating system as Version 1 and place the dedicated runtime under a future section. `agent/README.md` must state that a future UGC agent reads `SKILL.md`, schemas, templates, approved creator records, and approved campaign records.

- [ ] **Step 4: Add development dependency**

Create `requirements-dev.txt`:

```text
jsonschema>=4.23,<5
```

- [ ] **Step 5: Verify repository shell**

Run:

```bash
python - <<'PY'
from pathlib import Path
required = ["README.md", "AGENTS.md", "TASKS.md", "requirements-dev.txt", "agent/README.md"]
missing = [p for p in required if not Path(p).exists()]
assert not missing, missing
print("PASS")
PY
```

Expected: `PASS`.

- [ ] **Step 6: Commit**

```bash
git add README.md AGENTS.md TASKS.md requirements-dev.txt agent/README.md
git commit -m "docs: establish UGC repository operating boundaries"
```

---

### Task 2: Reusable UGC skill

**Files:**
- Create: `SKILL.md`

**Interfaces:**
- Consumes: repository boundaries from Task 1.
- Produces: reusable stage-based operating instructions consumed by Adley, Otto, and a future UGC agent.

- [ ] **Step 1: Write the skill front matter and trigger scope**

Use:

```yaml
---
name: ugc-agency-operations
description: Run agency UGC work from creator discovery through qualification, outreach, campaign controls, rights, approvals, performance review, and renewal decisions.
---
```

- [ ] **Step 2: Define the skill workflow states**

The skill must recognize exactly these stages:

```text
discovery
qualification
outreach
response_tracking
selection
campaign_brief
script_development
commercial_terms
rights_clearance
delivery
quality_review
deployment_handoff
performance_review
scorecard
renewal_decision
```

For every stage, state required inputs, allowed outputs, blocking conditions, and the next valid stage.

- [ ] **Step 3: Add evidence and claims rules**

The skill must use these evidence states:

```text
creator_provided
agency_observed
verified
unknown
```

It must prohibit converting `creator_provided` into `verified` without independent evidence.

- [ ] **Step 4: Add rights and approval gates**

Require separate fields for organic posting rights, brand usage rights, paid media rights, whitelisting/partnership-ad access, start date, and end date. Paid deployment must require `paid_media_rights = approved`, unexpired dates when dates apply, and final approval.

- [ ] **Step 5: Add scoring and routing rules**

Qualification must consider audience fit, content quality, brand fit, communication, reliability, category experience, engagement quality, available performance proof, deliverable fit, rate versus expected value, rights flexibility, paid-media suitability, and known conflict risk. The skill must state that follower count alone is not a decision rule.

Route content concepts/scripts to Adley, broader campaign/brand strategy to Creative Operating System, video production to AI Video, scaled publishing to Content Scaling, and workflow routing/audit work to Otto.

- [ ] **Step 6: Add Kristina reference prohibition**

Include this exact rule:

```markdown
Files under `examples/` are reference material only. They may inform presentation ideas, but they must never define creator scoring, qualification thresholds, price expectations, campaign requirements, or workflow rules.
```

- [ ] **Step 7: Verify required skill terms**

Run:

```bash
python - <<'PY'
from pathlib import Path
text = Path("SKILL.md").read_text()
required = [
    "creator_provided", "agency_observed", "verified", "unknown",
    "paid media rights", "follower count", "examples/", "renewal_decision"
]
missing = [x for x in required if x.lower() not in text.lower()]
assert not missing, missing
print("PASS")
PY
```

Expected: `PASS`.

- [ ] **Step 8: Commit**

```bash
git add SKILL.md
git commit -m "feat: add reusable agency UGC skill"
```

---

### Task 3: Creator contract, qualification model, and discovery workflow

**Files:**
- Create: `schemas/creator.schema.json`
- Create: `docs/creator-discovery.md`
- Create: `templates/creator-profile.md`
- Create: `tests/fixtures/valid-creator.json`

**Interfaces:**
- Consumes: evidence states and qualification factors from `SKILL.md`.
- Produces: structured creator records used by campaign records and creator scorecards.

- [ ] **Step 1: Define creator schema fields**

Require at minimum:

```json
{
  "creator_id": "creator-001",
  "display_name": "Example Creator",
  "platforms": [{"platform": "tiktok", "handle": "@example"}],
  "categories": ["home"],
  "location": "Dallas, TX",
  "evidence": [],
  "qualification": {
    "audience_fit": 4,
    "content_quality": 4,
    "brand_fit": 5,
    "communication_quality": 3,
    "reliability": null,
    "category_experience": 4,
    "engagement_quality": 3,
    "performance_proof": 2,
    "deliverable_fit": 5,
    "value_fit": 3,
    "rights_flexibility": 3,
    "paid_media_suitability": 4,
    "conflict_risk": "unknown"
  },
  "status": "qualified"
}
```

Scores use integers 1 through 5 or `null` when unknown. `conflict_risk` accepts `low`, `medium`, `high`, or `unknown`. `status` accepts `discovered`, `researching`, `qualified`, `not_qualified`, `selected`, `inactive`.

- [ ] **Step 2: Define evidence object rules**

Each evidence item must include `field`, `value`, `state`, `source`, and `captured_at`. `state` must be one of the four skill evidence states.

- [ ] **Step 3: Write discovery documentation and profile template**

Document source capture, unknown handling, conflict checks, and qualification review. The template must visibly separate facts from creator claims and agency observations.

- [ ] **Step 4: Create a valid creator fixture**

Use the example shape above with at least one `creator_provided` evidence item and one `agency_observed` item. Do not use Kristina data in the fixture.

- [ ] **Step 5: Commit**

```bash
git add schemas/creator.schema.json docs/creator-discovery.md templates/creator-profile.md tests/fixtures/valid-creator.json
git commit -m "feat: add creator qualification contract"
```

---

### Task 4: Campaign, rights, outreach, and approval contracts

**Files:**
- Create: `schemas/campaign.schema.json`
- Create: `docs/creator-outreach.md`
- Create: `docs/campaign-workflow.md`
- Create: `docs/rights-and-usage.md`
- Create: `templates/outreach-message.md`
- Create: `templates/ugc-campaign-brief.md`
- Create: `templates/script-brief.md`
- Create: `templates/rights-agreement-checklist.md`
- Create: `tests/fixtures/valid-campaign.json`

**Interfaces:**
- Consumes: `creator_id` from creator records.
- Produces: campaign records used by the validator, deployment handoffs, and performance records.

- [ ] **Step 1: Define required campaign fields**

The schema must require:

```text
campaign_id
creator_id
objective
audience
product_or_service
offer
primary_promise
cta
concept
deliverables
due_dates
revision_terms
rate
payment_terms
required_disclosures
prohibited_claims
rights
approvals
deployment_destination
measurement_plan
status
```

- [ ] **Step 2: Define rights object**

Use explicit states:

```json
{
  "organic_posting": "approved",
  "brand_usage": "approved",
  "paid_media": "approved",
  "whitelisting": "not_required",
  "start_date": "2026-08-14",
  "end_date": "2026-11-14"
}
```

Permission values accept `approved`, `not_approved`, `not_required`, `unknown`. Dates accept ISO `YYYY-MM-DD` strings or `null` only when the associated permission does not require a dated grant.

- [ ] **Step 3: Define approval states**

Require `strategy`, `creative`, `brand`, `quality`, `media`, and `final`. Each accepts `pending`, `approved`, `rejected`, `not_required`.

- [ ] **Step 4: Write campaign and rights docs**

Document the full stage flow, approval ownership, revision handling, rights expiration, disclosures, prohibited claims, exclusivity/conflicts, and deployment handoff. State that a creator agreeing to make content does not imply any paid-media usage right.

- [ ] **Step 5: Write outreach and operating templates**

Outreach templates must support initial outreach, follow-up, qualification questions, rate request, rights clarification, and decline/closeout. Campaign and rights templates must expose every required schema field.

- [ ] **Step 6: Create valid campaign fixture**

Use fictional data only. Set all required launch approvals to `approved`, paid-media rights to `approved`, and rights dates to a non-expired test range.

- [ ] **Step 7: Commit**

```bash
git add schemas/campaign.schema.json docs/creator-outreach.md docs/campaign-workflow.md docs/rights-and-usage.md templates/outreach-message.md templates/ugc-campaign-brief.md templates/script-brief.md templates/rights-agreement-checklist.md tests/fixtures/valid-campaign.json
git commit -m "feat: add UGC campaign rights and approval workflow"
```

---

### Task 5: Performance and creator scorecard contracts

**Files:**
- Create: `schemas/performance.schema.json`
- Create: `schemas/scorecard.schema.json`
- Create: `docs/measurement.md`
- Create: `templates/creator-scorecard.md`
- Create: `tests/fixtures/valid-performance.json`
- Create: `tests/fixtures/valid-scorecard.json`

**Interfaces:**
- Consumes: `campaign_id` and `creator_id`.
- Produces: objective-specific performance evidence and one defined renewal decision.

- [ ] **Step 1: Define performance schema**

Support nullable metrics for:

```text
views
reach
hook_rate
hold_rate
average_watch_time_seconds
completion_rate
likes
comments
shares
saves
ctr
leads
purchases
revenue
cost_per_lead
cost_per_acquisition
roas
affiliate_revenue
```

Require `campaign_id`, `creator_id`, `objective`, `captured_at`, `metrics`, and `evidence_sources`. Numeric values must never default to zero solely because data is missing.

- [ ] **Step 2: Define scorecard schema**

Require qualification summary, campaign operating experience, content quality, approval performance, delivery reliability, rights flexibility, audience response, business results, cost efficiency, reusable learning, and `decision`.

`decision` must be exactly one of:

```text
renew
retain_specific_use
retest_new_variable
pause
retire
```

- [ ] **Step 3: Write measurement rules**

Map objectives to relevant metrics. For example, awareness uses reach/views/watch metrics, traffic uses CTR/click evidence, leads use lead and CPL metrics, sales uses purchases/revenue/CPA/ROAS, and affiliate work uses attributable affiliate revenue when available. Unknown metrics stay unknown.

- [ ] **Step 4: Write creator scorecard template**

The template must separate pre-campaign qualification from in-campaign operating performance and business outcomes.

- [ ] **Step 5: Create valid performance and scorecard fixtures**

Use fictional values. Include at least two `null` metrics in the performance fixture to prove missing values remain unknown.

- [ ] **Step 6: Commit**

```bash
git add schemas/performance.schema.json schemas/scorecard.schema.json docs/measurement.md templates/creator-scorecard.md tests/fixtures/valid-performance.json tests/fixtures/valid-scorecard.json
git commit -m "feat: add UGC performance and scorecard contracts"
```

---

### Task 6: Validator and test suite

**Files:**
- Create: `scripts/validate_record.py`
- Create: `tests/test_validate_record.py`

**Interfaces:**
- Consumes: four JSON schemas and fixture records.
- Produces: CLI validation command with exit code `0` for valid records and `1` for blocked records.

- [ ] **Step 1: Write failing schema-loading test**

Start with:

```python
import unittest
from pathlib import Path

from scripts.validate_record import load_schema

class ValidationTests(unittest.TestCase):
    def test_load_creator_schema(self):
        schema = load_schema("creator")
        self.assertEqual(schema["$id"], "https://ugc.local/schemas/creator.schema.json")
```

- [ ] **Step 2: Run test and confirm failure**

Run:

```bash
python -m unittest tests.test_validate_record.ValidationTests.test_load_creator_schema -v
```

Expected: FAIL because `scripts.validate_record` does not exist.

- [ ] **Step 3: Implement schema loader**

Use:

```python
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = {
    "creator": ROOT / "schemas" / "creator.schema.json",
    "campaign": ROOT / "schemas" / "campaign.schema.json",
    "performance": ROOT / "schemas" / "performance.schema.json",
    "scorecard": ROOT / "schemas" / "scorecard.schema.json",
}

def load_schema(record_type: str) -> dict:
    path = SCHEMAS[record_type]
    return json.loads(path.read_text())
```

- [ ] **Step 4: Add failing business-rule tests**

Add tests proving these cases are blocked:

```text
campaign paid deployment with paid_media != approved
campaign paid deployment with final approval != approved
campaign with rights end_date before start_date
campaign with expired paid-media rights as of supplied validation date
creator evidence state outside the four allowed states
performance metric missing represented by an invented zero instead of null when source marks it unknown
scorecard decision outside the five defined states
reference metadata missing reference_only=true
```

Also add passing tests for all four valid fixtures.

- [ ] **Step 5: Implement `validate_record` and custom rules**

Provide this interface:

```python
def validate_record(record_type: str, payload: dict, *, as_of: str | None = None) -> list[str]:
    """Return a list of validation errors. Empty list means valid."""
```

Use `jsonschema.Draft202012Validator` for schema errors, then apply campaign rights/approval/date rules and the reference-only metadata rule.

- [ ] **Step 6: Implement CLI**

Support:

```bash
python scripts/validate_record.py creator tests/fixtures/valid-creator.json
python scripts/validate_record.py campaign tests/fixtures/valid-campaign.json --as-of 2026-08-14
python scripts/validate_record.py performance tests/fixtures/valid-performance.json
python scripts/validate_record.py scorecard tests/fixtures/valid-scorecard.json
```

Print `PASS` on success. Print one `ERROR: ...` line per failure and exit `1` on failure.

- [ ] **Step 7: Run full test suite**

Run:

```bash
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
```

Expected: all tests PASS.

- [ ] **Step 8: Commit**

```bash
git add scripts/validate_record.py tests/test_validate_record.py
git commit -m "test: add UGC record validation gates"
```

---

### Task 7: Media-kit template and Kristina reference example

**Files:**
- Create: `templates/media-kit-template.md`
- Create: `examples/media-kits/README.md`
- Add binary: `examples/media-kits/creator-paid-pitch-example-kristina-elise.pdf`

**Interfaces:**
- Consumes: uploaded source file `/mnt/data/Kristina Elise UGC Media Kit.pdf`.
- Produces: one unchanged reference PDF plus a neutral reusable pitch template. Neither file affects skill scoring.

- [ ] **Step 1: Write reference README before adding the PDF**

It must begin with:

```markdown
# Media Kit Examples

Reference example only. This media kit does not define UGC operating standards or scoring rules.
```

Document the source filename, repository filename, purpose, and `reference_only: true`. State that examples may be studied for presentation structure, proof packaging, service positioning, analytics presentation, partnership categories, and creator-side sales messaging only.

- [ ] **Step 2: Write neutral media-kit template**

Include sections for creator identity, positioning, audience/platforms, content categories, services, selected proof, analytics, partnership options, prior brand work, rights availability, and contact details. Do not copy Kristina's wording, metrics, pricing, or qualification assumptions.

- [ ] **Step 3: Add the uploaded PDF unchanged**

Copy:

```text
/mnt/data/Kristina Elise UGC Media Kit.pdf
```

to:

```text
examples/media-kits/creator-paid-pitch-example-kristina-elise.pdf
```

Expected SHA-256 of the uploaded source:

```text
7a7758b7fe34d25266e3aef64db3d03cbd86fee14281be1125d36e85ce77fb66
```

- [ ] **Step 4: Verify the binary stayed unchanged**

Run:

```bash
python - <<'PY'
from hashlib import sha256
from pathlib import Path
p = Path("examples/media-kits/creator-paid-pitch-example-kristina-elise.pdf")
assert sha256(p.read_bytes()).hexdigest() == "7a7758b7fe34d25266e3aef64db3d03cbd86fee14281be1125d36e85ce77fb66"
print("PASS")
PY
```

Expected: `PASS`.

- [ ] **Step 5: Add reference metadata test**

Extend `tests/test_validate_record.py` to assert `examples/media-kits/README.md` contains both `reference_only: true` and the sentence `does not define UGC operating standards or scoring rules`.

- [ ] **Step 6: Run tests**

```bash
python -m unittest discover -s tests -v
```

Expected: all tests PASS.

- [ ] **Step 7: Commit**

```bash
git add templates/media-kit-template.md examples/media-kits/README.md examples/media-kits/creator-paid-pitch-example-kristina-elise.pdf tests/test_validate_record.py
git commit -m "docs: add UGC media kit reference and template"
```

---

### Task 8: Final integration verification

**Files:**
- Modify: `README.md`
- Modify: `TASKS.md`

**Interfaces:**
- Consumes: all Version 1 files.
- Produces: verified repository with complete operating instructions and no undocumented workflow stages.

- [ ] **Step 1: Add validation commands to README**

Document:

```bash
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
python scripts/validate_record.py creator tests/fixtures/valid-creator.json
python scripts/validate_record.py campaign tests/fixtures/valid-campaign.json --as-of 2026-08-14
python scripts/validate_record.py performance tests/fixtures/valid-performance.json
python scripts/validate_record.py scorecard tests/fixtures/valid-scorecard.json
```

- [ ] **Step 2: Mark completed Version 1 items in TASKS.md**

Keep the dedicated UGC runtime, memory, scheduler, and autonomous execution under a future section rather than marking them complete.

- [ ] **Step 3: Run structural verification**

Run:

```bash
python - <<'PY'
from pathlib import Path
required = [
    "SKILL.md",
    "docs/creator-discovery.md",
    "docs/creator-outreach.md",
    "docs/campaign-workflow.md",
    "docs/rights-and-usage.md",
    "docs/measurement.md",
    "schemas/creator.schema.json",
    "schemas/campaign.schema.json",
    "schemas/performance.schema.json",
    "schemas/scorecard.schema.json",
    "templates/creator-profile.md",
    "templates/creator-scorecard.md",
    "templates/outreach-message.md",
    "templates/ugc-campaign-brief.md",
    "templates/script-brief.md",
    "templates/rights-agreement-checklist.md",
    "templates/media-kit-template.md",
    "examples/media-kits/README.md",
    "examples/media-kits/creator-paid-pitch-example-kristina-elise.pdf",
    "scripts/validate_record.py",
    "tests/test_validate_record.py",
    "agent/README.md",
]
missing = [p for p in required if not Path(p).exists()]
assert not missing, missing
print("PASS")
PY
```

Expected: `PASS`.

- [ ] **Step 4: Run final tests**

```bash
python -m unittest discover -s tests -v
```

Expected: all tests PASS.

- [ ] **Step 5: Run reference-only guard check**

```bash
python - <<'PY'
from pathlib import Path
skill = Path("SKILL.md").read_text().lower()
ref = Path("examples/media-kits/README.md").read_text().lower()
assert "examples/" in skill
assert "never define creator scoring" in skill or "must never define creator scoring" in skill
assert "reference_only: true" in ref
assert "does not define ugc operating standards or scoring rules" in ref
print("PASS")
PY
```

Expected: `PASS`.

- [ ] **Step 6: Commit final integration**

```bash
git add README.md TASKS.md
git commit -m "chore: complete UGC operating system v1"
```

---

## Self-Review Results

- Spec coverage: all approved Version 1 workflow stages map to a task.
- Reference isolation: the Kristina media kit has an explicit reference-only gate, unchanged binary verification, and no role in scoring logic.
- Ownership boundaries: specialist repositories remain owners of their existing systems.
- Type consistency: creator, campaign, performance, and scorecard IDs and decision states are stable across tasks.
- Testing: schema validation, cross-field rights gates, approval gates, unknown metrics, defined decision states, and reference-only metadata are covered.
- Future scope: dedicated UGC runtime and memory remain deferred until volume or complexity warrants them.
