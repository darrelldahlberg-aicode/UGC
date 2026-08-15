# Creator Discovery and Qualification

## Purpose

Find creators who fit the campaign and preserve what is known, claimed, observed, verified, or still unknown before any paid engagement decision.

## Discovery Inputs

Start with:

- target audience
- campaign category
- product or service
- desired platform or format
- deliverable type
- geography when relevant
- whether creator posting, brand-owned UGC, paid media, or a mix is expected
- known budget range when approved

## Evidence Capture

Every evidence item must record:

- `field`
- `value`
- `state`
- `source`
- `captured_at`

Allowed evidence states are:

- `creator_provided`
- `agency_observed`
- `verified`
- `unknown`

A creator claim stays `creator_provided` until independent evidence supports changing it. Publicly visible content may support `agency_observed`, but public visibility alone does not verify private revenue, conversion, audience-demographic, or partnership claims.

## Source Quality

Prefer direct and recent sources. Preserve the source URL, file, message, or record used. When the source cannot support a claim, mark the claim `unknown` instead of filling the gap.

## Qualification Factors

Score each factor from 1 to 5 when there is enough evidence. Use `null` when unknown.

- audience fit
- content quality
- brand fit
- communication quality
- reliability
- category experience
- engagement quality
- performance proof
- deliverable fit
- value fit
- rights flexibility
- paid-media suitability

Record conflict risk separately as `low`, `medium`, `high`, or `unknown`.

Follower count is one fact, not the qualification decision.

## Conflict Checks

Review known:

- direct competitor relationships
- exclusivity restrictions
- category conflicts
- conflicting public claims or positioning
- paid-media restrictions

Unknown conflict information must remain `unknown` until resolved.

## Qualification Review

A creator may move to `qualified` only after the record has enough evidence to judge campaign fit. A high number of unknowns does not automatically disqualify a creator, but unresolved critical unknowns must block selection when they affect rights, conflicts, deliverability, or campaign fit.

## Output

Create a creator record matching `schemas/creator.schema.json` and use `templates/creator-profile.md` for the human-readable review.
