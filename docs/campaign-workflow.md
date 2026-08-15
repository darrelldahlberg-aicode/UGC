# UGC Campaign Workflow

## Full Stage Flow

1. discovery
2. qualification
3. outreach
4. response_tracking
5. selection
6. campaign_brief
7. script_development
8. commercial_terms
9. rights_clearance
10. delivery
11. quality_review
12. deployment_handoff
13. performance_review
14. scorecard
15. renewal_decision

## Approval Ownership

Every campaign record includes these approval states:

- strategy
- creative
- brand
- quality
- media
- final

The operating team must name the actual approval owner in its working process. The schema records approval state, not organizational authority.

Allowed approval states are:

- `pending`
- `approved`
- `rejected`
- `not_required`

Final deployment requires `final = approved`. A paid-media deployment also requires paid-media rights to be approved and unexpired.

## Campaign Brief Requirements

A campaign must define:

- campaign ID
- creator ID
- objective
- audience
- product or service
- offer
- primary promise
- CTA
- concept
- deliverables
- due dates
- revision terms
- rate
- payment terms
- required disclosures
- prohibited claims
- rights
- approvals
- deployment destination
- measurement plan
- status

## Revision Handling

Revision terms must be defined before production. A revision request should reference the approved brief, a quality problem, a missing requirement, or a blocked claim. New scope should be treated as new scope instead of being hidden inside a revision.

## Rights and Expiration

Rights are cleared before deployment. Start and end dates are tracked when a granted permission has a dated term. Expired rights block any use that depends on those rights.

A creator agreeing to make content does not imply any paid-media usage right.

## Disclosures and Claims

Required disclosures must appear where the campaign or platform requires them. Prohibited claims must remain prohibited through script development, quality review, and deployment.

## Exclusivity and Conflicts

Known conflicts or exclusivity limits must be resolved before selection or commercial commitment when they affect campaign use. Unknown conflict status remains unknown and is escalated when it affects launch safety.

## Deployment Handoff

After quality review, route the approved output to the owning system:

- organic or scaled publishing: Content Scaling when appropriate
- content/script work: Adley
- broader campaign/brand alignment: Creative Operating System
- production video work: AI Video
- workflow routing and audit trail: Otto

UGC retains the creator record, rights state, approval state, and performance link.
