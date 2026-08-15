---
name: ugc-agency-operations
description: Run agency UGC work from creator discovery through qualification, outreach, campaign controls, rights, approvals, performance review, and renewal decisions.
---

# UGC Agency Operations

Use this skill for agency UGC work involving creator discovery, qualification, outreach, creator-specific campaign operations, rights, approvals, performance review, or renewal decisions.

## Evidence States

Every creator fact or claim must remain in exactly one evidence state:

- `creator_provided`: supplied by the creator or creator representative and not independently verified
- `agency_observed`: directly observed by the agency, such as visible content quality or a public post
- `verified`: independently supported by reliable evidence
- `unknown`: not known or not supported by available evidence

Never convert `creator_provided` into `verified` without independent evidence. Never replace `unknown` with an estimate to make a record look complete.

## Workflow Stages

The skill recognizes exactly these stages:

### `discovery`
Required inputs: campaign category, target audience, platform needs, deliverable needs, geography if relevant.
Allowed outputs: candidate creator list with sources and evidence states.
Blocking conditions: no defined audience or creator need.
Next valid stage: `qualification`.

### `qualification`
Required inputs: creator profile, source evidence, campaign fit requirements.
Allowed outputs: qualification record, unknowns, conflict flags, pass or fail recommendation.
Blocking conditions: insufficient identity or source evidence to evaluate fit.
Next valid stage: `outreach` for qualified creators, or stop for not-qualified creators.

### `outreach`
Required inputs: qualified creator, approved outreach context, requested deliverables, timeline.
Allowed outputs: initial outreach, follow-up message, qualification questions, rate request.
Blocking conditions: creator has not passed qualification or outreach scope is not approved.
Next valid stage: `response_tracking`.

### `response_tracking`
Required inputs: outreach record and creator responses.
Allowed outputs: response status, unanswered questions, requested commercial details, follow-up action.
Blocking conditions: none beyond preserving the response accurately.
Next valid stage: `selection` when enough information exists to decide.

### `selection`
Required inputs: qualification record, creator response, deliverable fit, commercial information, known rights position.
Allowed outputs: selected, not selected, or needs more information.
Blocking conditions: unresolved critical fit, conflict, or rights issue.
Next valid stage: `campaign_brief` for selected creators.

### `campaign_brief`
Required inputs: creator, objective, audience, product or service, offer, primary promise, CTA, concept, deliverables, due dates.
Allowed outputs: complete UGC campaign brief.
Blocking conditions: missing required campaign fields.
Next valid stage: `script_development`.

### `script_development`
Required inputs: approved campaign brief, claims constraints, disclosure requirements, format needs.
Allowed outputs: hook directions, script brief, talking points, prohibited claims.
Blocking conditions: campaign brief is incomplete or claims/disclosure rules are unknown when required.
Next valid stage: `commercial_terms`.

### `commercial_terms`
Required inputs: rate, payment terms, revision terms, deliverables, due dates.
Allowed outputs: commercial-term record ready for approval.
Blocking conditions: rate, payment terms, or deliverable scope is missing.
Next valid stage: `rights_clearance`.

### `rights_clearance`
Required inputs: organic posting rights, brand usage rights, paid media rights, whitelisting or partnership-ad access, start date, end date, conflicts or exclusivity terms.
Allowed outputs: approved rights record or blocked rights record.
Blocking conditions: required permission is `unknown` or `not_approved`, required dates are missing, or rights are expired.
Next valid stage: `delivery` when required rights and terms are clear.

### `delivery`
Required inputs: approved brief, commercial terms, rights record, due dates.
Allowed outputs: delivery status, received assets, revision request, missing-item list.
Blocking conditions: required commercial or rights record is not approved.
Next valid stage: `quality_review`.

### `quality_review`
Required inputs: delivered assets, campaign brief, brand requirements, required disclosures, prohibited claims.
Allowed outputs: approved, revision required, or rejected with reasons.
Blocking conditions: missing asset, missing disclosure, prohibited claim, or unresolved quality defect.
Next valid stage: `deployment_handoff` after quality approval.

### `deployment_handoff`
Required inputs: approved asset, deployment destination, rights record, approval record.
Allowed outputs: specialist handoff for organic, brand-owned, or paid deployment.
Blocking conditions: missing or expired required rights, or final approval is not approved. Paid deployment additionally requires paid media rights = approved.
Next valid stage: `performance_review` after deployment evidence exists.

### `performance_review`
Required inputs: campaign objective, performance record, evidence sources.
Allowed outputs: objective-specific performance interpretation and unknown metric list.
Blocking conditions: no performance evidence source.
Next valid stage: `scorecard`.

### `scorecard`
Required inputs: creator qualification, operating experience, content quality, delivery reliability, rights flexibility, audience response, business results, cost efficiency, reusable learning.
Allowed outputs: complete creator scorecard.
Blocking conditions: campaign has not reached a reviewable outcome or unknowns are being replaced with invented values.
Next valid stage: `renewal_decision`.

### `renewal_decision`
Required inputs: completed scorecard and campaign evidence.
Allowed outputs: `renew`, `retain_specific_use`, `retest_new_variable`, `pause`, or `retire`.
Blocking conditions: no scorecard or unsupported decision rationale.
Next valid stage: end of current campaign cycle or a new `campaign_brief` for approved follow-up work.

## Creator Qualification Factors

Qualification must consider:

- audience fit
- content quality
- brand fit
- communication quality
- reliability
- category experience
- engagement quality
- available performance proof
- deliverable fit
- rate versus expected value
- rights flexibility
- paid-media suitability
- known conflict risk

Follower count alone is not a decision rule.

## Rights and Approval Gates

Track these separately:

- organic posting rights
- brand usage rights
- paid media rights
- whitelisting or partnership-ad access
- rights start date
- rights end date

Paid deployment requires paid media rights = approved, unexpired rights dates when dates apply, and final approval = approved. Organic posting rights do not imply brand usage rights or paid media rights.

## Specialist Routing

- Route content concepts, hooks, scripts, captions, and platform variants to Adley.
- Route broader campaign and brand strategy to Creative Operating System.
- Route video production, assembly, and production QA to AI Video.
- Route scaled publishing and content matrices to Content Scaling.
- Route workflow routing, retries, audit records, and orchestration to Otto.

This skill supplies creator-specific context and rules. It does not duplicate specialist logic.

## Reference Example Prohibition

Files under `examples/` are reference material only. They may inform presentation ideas, but they must never define creator scoring, qualification thresholds, price expectations, campaign requirements, or workflow rules.
