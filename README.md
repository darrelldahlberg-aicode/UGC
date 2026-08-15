# UGC Agency Operating System

This repository is the agency-facing source of truth for creator-specific UGC operations from discovery through renewal decisions.

UGC owns creator-specific operating rules, evidence handling, qualification, outreach, commercial terms, rights, approvals, performance review, and creator scorecards. Content Scaling, Creative Operating System, AI Video, Adley, Aaron, Kimberly, Stevie, and Otto retain their existing specialist responsibilities. This repository references those systems instead of duplicating them.

## Read Order
1. `AGENTS.md`
2. `SKILL.md`
3. `docs/production-operations.md`
4. `docs/first-live-campaign-runbook.md`
5. `docs/campaign-workflow.md`
6. `docs/rights-and-usage.md`
7. `docs/measurement.md`
8. `schemas/`
9. `templates/`

## Version 1 Workflow
Creator discovery -> qualification -> outreach -> response tracking -> selection -> campaign brief -> hooks/scripts -> rates/payment -> rights -> delivery -> QA/approval -> deployment handoff -> performance -> scorecard -> renew/retest/pause/retire.

## Repository Ownership

This repository owns:

- creator discovery and qualification rules
- creator evidence states and records
- outreach and response tracking standards
- creator-specific campaign briefs
- commercial-term records
- usage-rights and paid-media permission gates
- approval gates
- UGC measurement rules
- creator scorecards and renewal decisions
- neutral reusable media-kit templates
- reference-only media-kit examples

This repository does not own:

- scaled publishing systems from Content Scaling
- broad campaign and brand strategy from Creative Operating System
- video production and assembly from AI Video
- Adley-specific content behavior
- Aaron-specific paid-media behavior
- Kimberly-specific quality-control behavior
- Stevie-specific strategy behavior
- Otto-specific routing, retries, or audit runtime

## Production Operations

Production approval ownership and durable-record storage rules are locked in `docs/production-operations.md`.

Key rules:

- Stevie owns strategy preparation and review.
- Adley owns creator-specific creative development.
- Kimberly owns brand consistency, quality control, and release-readiness review.
- Aaron owns paid-media review.
- Otto owns final internal workflow approval.
- Darrell or an authorized human administrator approves restricted actions including publishing, production deployment, spend, campaign activation, pricing, contracts, and payment commitments.
- Live client UGC records belong in the approved client repository, not in this UGC repository or an agent repository.
- AiAgentWorkspace remains the control and routing layer and should carry references rather than raw live UGC records.

The first live campaign should follow `docs/first-live-campaign-runbook.md`.

## Evidence Standard

Creator information must remain in one of four evidence states until independently changed by evidence:

- `creator_provided`
- `agency_observed`
- `verified`
- `unknown`

Creator-provided claims do not become verified facts without independent evidence. Missing metrics remain unknown and are not estimated.

## Rights Standard

Organic posting rights, brand usage rights, paid media rights, and whitelisting or partnership-ad access are separate permissions. Approval to create content does not imply approval to use the content in paid media.

## Reference Example Rule

Files under `examples/` are reference-only. They may help with presentation structure, proof packaging, service positioning, analytics presentation, partnership categories, and creator-side sales messaging. They do not define creator scoring, qualification thresholds, price expectations, campaign requirements, or workflow rules.

## Validation

Install the development dependency and run the full test suite:

```bash
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
```

Validate individual records:

```bash
python scripts/validate_record.py creator tests/fixtures/valid-creator.json
python scripts/validate_record.py campaign tests/fixtures/valid-campaign.json --as-of 2026-08-14
python scripts/validate_record.py performance tests/fixtures/valid-performance.json
python scripts/validate_record.py scorecard tests/fixtures/valid-scorecard.json
```

A valid record prints `PASS`. Invalid records print one `ERROR: ...` line per failure and exit with status `1`.

## Current Status

The skill-first UGC operating system is production-ready for a first real creator campaign. The only live activation item is running the system against an actual creator and campaign. That step must use real evidence and must not be simulated with the Kristina reference example.

## Future Dedicated Agent

Version 1 is skill-first. A dedicated UGC runtime, memory system, scheduler, or autonomous execution layer is deferred until campaign volume or workflow complexity warrants it. See `agent/README.md`.
