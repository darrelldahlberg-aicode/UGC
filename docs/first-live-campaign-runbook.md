# First Live UGC Campaign Runbook

## Goal

Run the first live creator campaign through the Version 1 system without skipping qualification, rights, approvals, storage, or measurement.

## Before Outreach

- Confirm an approved client repository exists.
- Confirm the shared client record exists and identifies the client.
- Confirm campaign objective, audience, product or service, offer, CTA, deliverable need, and budget boundary.
- Create the creator record under `ugc/creators/` in the client repository.
- Validate the creator record with the UGC creator schema.

## 1. Discovery

Capture creator identity, platforms, category fit, source links, visible content observations, and unknowns.

Keep evidence states separate:

- `creator_provided`
- `agency_observed`
- `verified`
- `unknown`

Do not use the Kristina media-kit example as a qualification threshold.

## 2. Qualification

Evaluate all qualification factors in `SKILL.md`.

Record the decision as qualified, not qualified, or needing more evidence. Follower count alone does not qualify a creator.

## 3. Outreach

Adley may prepare the outreach message. Do not promise rates, paid usage, volume, or contract terms that have not been approved.

Before making a paid commitment, Darrell or an authorized human administrator must approve the commercial boundary.

## 4. Selection

Select the creator only after campaign fit, deliverable fit, known conflicts, rate expectations, and likely rights availability are understood.

## 5. Campaign Brief

Create the campaign record under:

`ugc/campaigns/<campaign-id>.json`

The brief must include the complete objective, audience, product or service, offer, promise, CTA, concept, deliverables, due dates, revision terms, disclosures, prohibited claims, deployment destination, and measurement plan.

## 6. Script and Creative

Adley owns concepts, hooks, scripts, captions, and creator-specific content direction.

Kimberly reviews brand consistency, human writing quality, and release readiness.

## 7. Commercial Terms and Rights

Record:

- creator rate
- payment terms
- revision terms
- organic posting rights
- brand usage rights
- paid-media rights
- whitelisting or partnership-ad access
- rights start date
- rights end date
- exclusivity terms if any

Darrell or an authorized human administrator approves spend, pricing, contract, and payment commitments.

Never infer paid-media rights from organic rights.

## 8. Delivery and QA

Track received assets and revisions.

Kimberly owns quality review. Block the asset for missing disclosures, prohibited claims, brand conflicts, or unresolved quality issues.

## 9. Media Review

If content will run as paid media, Aaron reviews media suitability, tracking, attribution needs, and deployment context.

Paid deployment requires approved paid-media rights.

## 10. Final Approval

Otto grants final internal workflow approval after required specialist reviews are complete.

Darrell or an authorized human administrator grants any required approval for publishing, production activation, spend, contracts, or other restricted actions.

## 11. Deployment Handoff

Route the approved output to the owning system:

- paid media to Aaron
- scaled publishing to Content Scaling
- video production work to AI Video
- workflow routing and audit to Otto

UGC does not duplicate those runtimes.

## 12. Performance Record

Create:

`ugc/performance/<campaign-id>.json`

Record only objective-relevant metrics. Missing metrics remain `null` or explicitly unknown. Do not estimate them.

## 13. Creator Scorecard

Create:

`ugc/scorecards/<campaign-id>.json`

Score the creator using pre-campaign fit, operating performance, content quality, delivery reliability, rights flexibility, audience response, business results, and cost efficiency.

## 14. Renewal Decision

Choose one defined outcome:

- `renew`
- `retain_specific_use`
- `retest_new_variable`
- `pause`
- `retire`

Record the decision reason and reusable learning.

## 15. Closeout

Before marking the campaign complete, confirm:

- all durable records exist in the client repository
- shared client record references current task, approval, result, and deadline status where needed
- payment obligations are recorded
- rights expiration is recorded
- performance evidence is stored
- scorecard decision is complete
- no private live campaign record was stored in the UGC or agent repositories

## First Campaign Success Condition

The first live campaign validates Version 1 when every stage above has a traceable record and no required approval, rights gate, or evidence state is bypassed.
