---
id: MADR-001
title: "Distinguishing Implemented from Delivered Status for REQ-001"
status: accepted
service: platform
milestone: v1.0
date: 2026-04-20
deciders:
  - "Agent: curupira-companion (Architect role)"
  - "@nuneslucioliveira"
---

# MADR-001: Distinguishing Implemented from Delivered Status for REQ-001

> **Classification:** This is a Meta-ADR (MADR) addressing methodology and process questions about the SDD lifecycle, not an implementation-directed ADR.

## Context and Problem Statement

REQ-001 is currently at `status: implemented` with all six acceptance criteria tested. ADR-001 is at `status: accepted`. The question is: what evidence or artifacts would move REQ-001 from `implemented` to `delivered`?

**Current State Analysis:**

- REQ-001 status: `implemented`
- ADR-001 status: `accepted`
- All ACs (AC-001 through AC-006) have test coverage
- Related ADRs are complete and accepted

**Problem:** The distinction between `implemented` and `delivered` requires clarification to establish what constitutes production readiness versus code completion.

## Considered Options

1. **Deploy-and-Declare Model:** Transition to `delivered` upon deployment to production environment, requiring only operational deployment evidence.

2. **Evidence-Complete Model:** Transition to `delivered` upon accumulation of comprehensive testing artifacts including unit tests, integration tests, performance benchmarks, and security audit evidence.

3. **Hybrid Model:** Transition to `delivered` upon deployment AND minimum threshold of testing artifacts (AC coverage proof, performance baseline evidence).

## Decision Outcome

Chosen option: **Hybrid Model**, because it balances operational reality with quality assurance requirements without creating undue friction.

### Rationale

The SDD methodology lifecycle (methodology.md) explicitly states:

> "`status: implemented` — Developer sets when PR merged and tests passing. Milestone not yet in production."
> "`status: delievered` — PM sets when milestone in production. Feature live for users."

However, for documentation and knowledge preservation purposes, establishing a clear evidence boundary is valuable even when the milestone hasn't been production-deployed.

### Consequences

**Good, because:** This approach provides operational clarity — a feature is truly delivered only when users can access it in production.

**Good, because:** It maintains separation of concerns between developer responsibility (implementation + tests) and product ownership (release + user availability).

**Bad, because:** For single-milestone projects like v1.0 CLI tool, the delay between implemented and delivered may obscure actual completion state — *mitigated/acceptable: This is intentional; the distinction serves audit and knowledge management purposes.*

**Neutral, because:** The current status `implemented` accurately reflects the state of the codebase — merged, tested, but not yet in production.

## Implementation Notes

### For REQ-001 Status Management

REQ-001 should remain at `status: implemented` until:

1. **Operational Deployment:** The CLI tool is deployed to its target environment (user's machine, package registry, or production service)
2. **User Access:** At least one end-user can access and use the feature
3. **Milestone Closure:** v1.0 milestone is formally released

### For Documentation Purposes

This MADR serves as the authoritative explanation of:

1. Why REQ-001 is marked `implemented` rather than `delivered`
2. What evidence would be required for `delivered` status
3. The role of PM vs Developer in status transitions

### Status Transition Workflow

```
REQ-001: draft → accepted (PM approval) → implemented (Dev: PR merged + tests passing) → delivered (PM: production + milestone live)
```

**Developer responsibilities (to reach `implemented`):**
- Complete all functional requirements
- Write tests covering all acceptance criteria
- Merge PR into main branch
- Verify tests pass in CI

**Product Owner responsibilities (to reach `delivered`):**
- Deploy to production environment
- Verify milestone release is live
- Notify stakeholders of feature availability
- Update `status: delivered` in REQ document

## Sources

- REQ-001 current status and completion state
- ADR-001 accepted status
- methodology.md: Document Status Lifecycles (REQ and ADR sections)
- AGENTS.md: Status field valid values and gating rules

---

## Related Artifacts

- REQ-001: CLI Basic Password Generation
- ADR-001: Python standard library cryptographic decision
- methodology.md: SDD lifecycle and status definitions
