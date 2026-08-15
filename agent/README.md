# Future UGC Agent Boundary

Version 1 does not create a separate UGC runtime, memory system, scheduler, or autonomous execution layer.

A future dedicated UGC agent must read and follow:

- `SKILL.md`
- the JSON schemas in `schemas/`
- the reusable files in `templates/`
- approved creator records
- approved campaign records
- approved performance records
- approved scorecards

## Activation Criteria

A dedicated runtime should be considered only when creator volume, campaign volume, response tracking, rights expirations, or approval routing become large enough to justify autonomous execution.

## Future Responsibilities

The future agent may:

- identify the current UGC workflow stage
- validate records before transitions
- route creator work to the correct specialist system
- flag missing evidence, rights, dates, approvals, or performance records
- track rights expiration and campaign status
- preserve creator scorecard decisions and reusable learning

It must not create parallel scoring rules, duplicated prompts, or a separate UGC policy layer. Shared rules remain in this repository.
