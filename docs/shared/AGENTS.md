# AGENTS.md - Shared Docs

## Repository Layout

| Path | Purpose |
|---|---|
| `architecture/adrs/` | Architectural decisions scoped to services and platform |
| `requirements/` | Product requirements (REQs) organized by domain |
| `workflows/` | Step-by-step contribution guides |
| `methodology.md` | SDD lifecycle and vocabulary |

## How to Read Requirements (REQs)

Navigate the REQs in this order:

1. **Domain Index:** `requirements/index-<domain>.md`
2. **REQ File:** `REQ-NNN-<title>.md`
3. **Related ADRs:** Check `related-adrs` field
4. **ADR Files:** `architecture/adrs/NNN-<title>.md`

## How to Read ADRs

Navigate ADRs in this order:

1. **Service Index:** `architecture/adrs/index-<service>.md`
2. **ADR File:** `NNN-<title>.md`

**Implementation Notes:** Always read ADR `Implementation Notes` before writing code.

## REQ Frontmatter Fields

| Field | Valid Values |
|---|---|
| `status` | `draft` \| `accepted` \| `implemented` \| `delivered` \| `cancelled` \| `superseded` |
| `milestone` | See [`../README.md#milestone`](../README.md#milestone) |
| `requires` | Other REQ IDs that must be implemented first |
| `related-adrs` | ADR IDs that govern implementation choices |
| `blocked-by` | Free-text signal — do not implement if populated |

## ADR Frontmatter Fields

| Field | Valid Values |
|---|---|
| `status` | `proposed` \| `accepted` \| `deprecated` \| `superseded by ADR-NNN` |
| `service` | Service name from [`architecture/overview.md`](architecture/overview.md) or `platform` |
| `related-reqs` | REQ IDs that motivated this decision |
| `impacts` | ADR IDs that may need review if this changes |

## Authoring Rules

### REQ Hard Stops

- Never set `status: accepted` without PM approval
- Zero `TBD`/`TO-DO` in `accepted`, `implemented`, or `delivered` status
- `author` field is append-only — never remove entries

### ADR Hard Stops

- Never set `status: accepted` without Architect approval
- Zero `TBD`/`TO-DO` in `accepted` status
- `deciders` must list actual humans, not just agents

## Branching Strategy

This project uses **Trunk-based (main only + short-lived feature branches)**.

- Feature branches branch from `main`
- Short-lived branches targeted at `main`
- No long-lived feature branches

## What NOT to Do

- Never implement a REQ with `status: draft`
- Never skip the D3 discernment step before delegation
- Never bundle `shared-docs` changes in a microservice PR
- Never merge directly to `main` without a PR
- Never set `status: accepted` autonomously
