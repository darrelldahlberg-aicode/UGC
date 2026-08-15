# UGC Agency Operating System Design

## Purpose

Build `darrelldahlberg-aicode/UGC` as the agency-facing source of truth for creator and UGC operations.

Version 1 covers the full workflow from creator discovery through campaign reporting and renewal decisions.

The repository will start with a reusable UGC skill and operating system. It will also reserve a clean boundary for a future dedicated UGC agent without duplicating the shared skill or operating rules.

## Core Architecture

The UGC repository owns reusable UGC strategy, workflows, templates, data contracts, scoring rules, rights controls, approvals, and measurement standards.

The initial system is skill-first. `SKILL.md` is the primary reusable instruction layer for Adley, Otto, and other approved agents. A future dedicated UGC agent will consume the same rules rather than create its own parallel system.

The UGC repository does not duplicate the responsibilities of Content Scaling, Creative Operating System, AI Video, or agent-specific repositories.

## Version 1 Workflow

1. Creator discovery
2. Creator qualification
3. Outreach
4. Response tracking
5. Creator selection
6. Campaign brief
7. Hook and script development
8. Rate and payment-term tracking
9. Usage-rights and paid-media permissions
10. Content delivery tracking
11. Quality review and approval
12. Organic or paid deployment handoff
13. Performance tracking
14. Creator scorecard
15. Renewal, retainer, or retirement decision

## Repository Ownership

The UGC repository owns:

- creator discovery standards
- creator qualification criteria
- outreach workflow and templates
- creator profiles
- creator scorecards
- UGC campaign briefs
- hook and script briefing standards
- rate and payment-term records
- usage-rights requirements
- organic posting rights
- paid media rights
- whitelisting or partnership-ad access records
- delivery tracking
- approval gates
- UGC performance measurement
- creator renewal rules
- UGC media-kit reference examples
- reusable media-kit templates for future agency or creator pitches

## Repository Boundaries

### Content Scaling

Content Scaling owns scaled publishing frameworks, topic generation, social matrices, and Creative Intelligence feedback loops. UGC supplies approved creator outputs and performance records when needed. It does not copy the Content Scaling system.

### Creative Operating System

Creative Operating System owns broad campaign strategy, brand systems, creative quality standards, and connected customer-journey rules. UGC consumes relevant approved campaign context and creator partnership standards while owning the detailed UGC workflow.

### Agent Adley Content

Adley creates content concepts, hooks, scripts, captions, and platform variants. The UGC skill gives Adley the creator-specific operating rules and approved campaign context. Adley's repository remains the home for Adley-specific behavior.

### AI Video

AI Video owns video production, provider routing, assembly, QA, distribution requirements, video analytics contracts, and ROI reporting. UGC hands approved video briefs or creator deliverables to AI Video when production work is required.

### Otto

Otto may route UGC tasks, approvals, retries, and handoffs. The UGC repository owns UGC operating rules. Otto does not duplicate them.

## Kristina Elise Media Kit Rule

The uploaded Kristina Elise UGC Media Kit is reference material only.

It serves two purposes:

1. A creator-side example of what a person seeking paid creator or UGC work may send to the agency.
2. A model of success and presentation structure for future UGC pitches or media kits the agency may create.

The Kristina media kit does not define, train, score, rank, or control the UGC skill.

No scoring rule, creator qualification threshold, payment recommendation, campaign standard, or workflow requirement may be derived from this example alone.

The example should be stored with a clear label such as:

`examples/media-kits/creator-paid-pitch-example-kristina-elise.pdf`

A companion README must state:

> Reference example only. This media kit does not define UGC operating standards or scoring rules.

The example may be studied for presentation structure, proof packaging, service positioning, analytics presentation, partnership categories, and creator-side sales messaging.

## Proposed Repository Structure

```text
UGC/
├── SKILL.md
├── README.md
├── AGENTS.md
├── TASKS.md
├── docs/
│   ├── creator-discovery.md
│   ├── creator-outreach.md
│   ├── campaign-workflow.md
│   ├── rights-and-usage.md
│   ├── measurement.md
│   └── superpowers/
│       ├── specs/
│       └── plans/
├── templates/
│   ├── creator-profile.md
│   ├── creator-scorecard.md
│   ├── outreach-message.md
│   ├── ugc-campaign-brief.md
│   ├── script-brief.md
│   ├── rights-agreement-checklist.md
│   └── media-kit-template.md
├── examples/
│   └── media-kits/
│       ├── README.md
│       └── creator-paid-pitch-example-kristina-elise.pdf
├── schemas/
│   ├── creator.schema.json
│   ├── campaign.schema.json
│   └── performance.schema.json
└── agent/
    └── README.md
```

## Skill Design

`SKILL.md` will be the reusable operating skill for agency UGC work.

The skill will:

- determine the current UGC workflow stage
- require creator qualification before paid engagement
- separate discovery evidence from assumptions
- preserve creator-provided claims as creator-provided until verified
- require campaign objective, audience, offer, CTA, deliverables, due dates, approvals, and rights before launch
- distinguish organic rights from paid media rights
- distinguish creator posting from brand-owned UGC
- track expiration dates for usage rights
- require approval before publishing or paid deployment
- score creator and campaign performance using defined metrics rather than follower count alone
- preserve performance evidence for future renewal decisions
- route work to existing specialist systems instead of duplicating their logic

## Creator Qualification Model

Version 1 will evaluate creators across multiple factors rather than use one follower threshold.

Factors include:

- audience fit
- content quality
- brand fit
- communication quality
- reliability
- relevant category experience
- engagement quality
- proof of past performance when available
- deliverable fit
- rate relative to expected value
- rights availability
- paid-media suitability when needed
- conflict or exclusivity risk

The system will clearly separate verified facts, creator-provided claims, agency observations, and unknowns.

## Campaign Controls

Every paid UGC campaign record must include:

- creator
- campaign objective
- audience
- product or service
- offer
- primary promise
- CTA
- content concept
- deliverables
- due dates
- revision terms
- rate
- payment terms
- required disclosures
- prohibited claims
- organic posting rights
- brand usage rights
- paid media rights
- whitelisting or partnership-ad permissions when applicable
- rights start date
- rights end date
- approval status
- deployment destination
- measurement plan

## Performance Model

Performance reporting will support both content and business outcomes.

Possible content metrics include:

- views
- reach
- hook rate
- hold rate
- average watch time
- completion rate
- likes
- comments
- shares
- saves
- click-through rate

Possible business metrics include:

- leads
- purchases
- revenue
- cost per lead
- cost per acquisition
- return on ad spend when paid media is used
- affiliate revenue when applicable

The skill will use only metrics relevant to the campaign objective. Missing metrics remain unknown rather than being estimated.

## Creator Scorecard

The creator scorecard will combine:

- pre-campaign qualification
- operating experience during the campaign
- content quality
- approval performance
- delivery reliability
- rights flexibility
- audience response
- business results
- cost efficiency
- reusable learning

The final decision will be one of:

- renew
- retain for specific use cases
- retest with a new variable
- pause
- retire

## Future Dedicated UGC Agent

The `agent/` directory reserves the future UGC agent architecture.

Version 1 will not build a separate runtime, memory system, or duplicated prompts.

A future UGC agent should consume:

- `SKILL.md`
- repository schemas
- approved templates
- scoring rules
- campaign records
- creator records

The dedicated agent should be added only when automation volume or workflow complexity makes a separate runtime worthwhile.

## Error and Safety Handling

The system must block or flag:

- missing usage rights
- expired rights
- unclear paid-media permissions
- unapproved claims
- missing disclosure requirements
- payment terms without an approval record
- creator conflicts or exclusivity concerns when known
- campaign deployment before required approvals
- invented creator performance data
- creator-provided claims presented as independently verified facts
- use of the Kristina reference example as a scoring or qualification standard

## Testing and Validation

Version 1 will include lightweight validation for structured creator, campaign, and performance records.

Tests should verify:

- required creator fields
- required campaign fields
- rights dates and permission states
- approval gating
- separation of creator-provided versus verified facts
- performance records preserve unknown metrics
- creator scorecard accepts only defined decision states
- Kristina example metadata is marked reference-only

## Success Criteria

Version 1 is complete when the repository contains:

- a reusable `SKILL.md`
- clear UGC workflow documentation
- creator discovery and qualification rules
- creator outreach templates
- campaign brief and script templates
- rights and payment tracking templates
- creator and campaign schemas
- performance and scorecard structure
- the Kristina media kit stored as a clearly labeled reference-only example
- a reusable media-kit template
- future UGC agent boundary documentation
- validation tests or equivalent checks for core structured records

The result must let the agency run a creator campaign from discovery through renewal without relying on undocumented steps or copying another repository's operating logic.
