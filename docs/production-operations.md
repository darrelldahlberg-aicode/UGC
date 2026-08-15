# UGC Production Operations

## Purpose

This document locks the approval ownership and durable-record storage rules for live UGC work.

## Approval Ownership

UGC follows the shared agency human-approval boundary.

### Strategy

- Stevie prepares and reviews business, offer, campaign, and growth strategy.
- Otto confirms the internal workflow is complete.
- Darrell or an authorized human administrator approves any strategy decision that activates spend, changes pricing or contracts, or creates another restricted external action.

### Creative

- Adley owns creator-facing content concepts, hooks, scripts, captions, and platform variants.
- Kimberly reviews release readiness and human writing quality.

### Brand

- Kimberly owns brand-consistency review.
- Brand approval must be recorded before public deployment when brand rules apply.

### Quality

- Kimberly owns quality-control review and release-readiness review.

### Media

- Aaron owns paid-media suitability, targeting, tracking, attribution, and media-specific review.
- Paid deployment is blocked until paid-media rights are approved and the required human approval is recorded.

### Commercial Terms

- Darrell or an authorized human administrator approves creator rates, payment commitments, contracts, usage-rights purchases, and other spend commitments.

### Final Internal Workflow Approval

- Otto owns final internal workflow approval after all required specialist reviews are complete.
- Otto does not replace human approval for restricted actions.

### Restricted Final Approval

Only Darrell or an authorized human administrator may approve:

- public publishing
- production deployment
- spending or campaign activation
- budget changes
- pricing or contracts
- external commitments involving payment or material terms
- destructive deletion
- material account changes

## Production Record Storage

### UGC Repository

`darrelldahlberg-aicode/UGC` stores only reusable operating rules, schemas, templates, validators, tests, and reference examples.

Do not store live client records, creator payment records, campaign results, credentials, or private client data in this repository.

### Durable Client Records

The durable source of truth for client-specific UGC records is the approved client repository.

Use this structure inside the client repository:

```text
ugc/
  creators/
    <creator-id>.json
  campaigns/
    <campaign-id>.json
  performance/
    <campaign-id>.json
  scorecards/
    <campaign-id>.json
  approvals/
    <campaign-id>.json
  outputs/
    <campaign-id>/
```

Records must use the schemas owned by this UGC repository.

### Shared Client Record

The agency shared client record remains governed by `darrelldahlberg-aicode/agency-agent-standards/contracts/client-record.schema.json`.

UGC-related tasks, approvals, results, and deadlines may be referenced from the shared client record. Do not duplicate full private creator or performance payloads there when a durable client-repository record already exists.

### AiAgentWorkspace

AiAgentWorkspace remains the control center and routing layer. It may store routing, status, approval references, audit references, and output references. It must not become the durable home for live UGC creator records or raw client performance data.

## Storage Rule When No Client Repository Exists

Do not place live client data in the UGC repository as a fallback.

If an approved client repository does not exist, create no durable UGC record until the proper client storage destination is established.

## Record Naming

Use stable IDs rather than creator names in machine records when possible:

- creator: `creator-<stable-id>`
- campaign: `ugc-<campaign-id>`
- performance: same campaign ID as the campaign record
- scorecard: same campaign ID as the campaign record

## Production Gate

A live UGC campaign may move to deployment only when:

1. creator qualification is complete
2. campaign brief is complete
3. commercial terms are human-approved
4. required rights are approved and unexpired
5. creative, brand, quality, and media approvals are complete where applicable
6. Otto grants final internal workflow approval
7. Darrell or an authorized human grants any required restricted-action approval
8. the durable client-record destination is known
