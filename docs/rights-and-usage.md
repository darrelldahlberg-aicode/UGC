# Rights and Usage

## Core Rule

Content creation permission and content usage permission are different. Every campaign must record the exact usage granted.

## Permission States

Each rights field accepts:

- `approved`
- `not_approved`
- `not_required`
- `unknown`

## Rights Fields

Track separately:

- `organic_posting`: permission or obligation for creator-posted organic content
- `brand_usage`: brand-owned organic or owned-channel usage
- `paid_media`: use of creator content in paid advertising
- `whitelisting`: whitelisting or partnership-ad access
- `start_date`
- `end_date`

## Date Rules

When a granted permission has a dated term, both dates must be present. `end_date` must not precede `start_date`. Any use after `end_date` is blocked until a renewal or extension is approved.

Dates may be `null` only when the associated permissions do not require a dated grant. If one or more active permissions are approved, the campaign should carry the applicable rights term.

## Paid Media Gate

Paid deployment requires:

- `paid_media = approved`
- applicable rights dates that are not expired
- final approval = approved
- any other required media or quality approval resolved

Organic posting permission does not imply paid media permission. Brand usage permission does not imply whitelisting permission.

## Whitelisting or Partnership Ads

If paid delivery uses the creator identity or account access, record whitelisting or partnership-ad permission explicitly. `unknown` is a blocker when the deployment requires it.

## Disclosures

Campaign records must list required disclosures. These requirements follow the campaign through script development, delivery, quality review, and deployment.

## Exclusivity and Conflicts

Record known exclusivity terms and creator conflicts when relevant. Do not infer a conflict-free status from silence.
