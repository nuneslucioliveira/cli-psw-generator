# Writing and Reviewing Documentation: Authoring Guide

## Who is this for?

| Persona | What you write |
|---|---|
| **PM/PO** | REQs (problem, scope, ACs) |
| **Architect** | ADRs (decisions, trade-offs) |
| **Designer** | Figma Make prompts (UI contracts) |

## Before you start

- [ ] Current branch is not `main` or `develop`
- [ ] REQ status is `accepted` (before Plan phase)
- [ ] All `related-adrs` are `accepted` (before Task phase)
- [ ] AC-derived tests exist (before Implement phase)
- [ ] Loading `sdd.md` and `ai-fluency.md` completed

---

## Writing a REQ

### Step 1 — Discovery prompt

Ask these questions to understand the problem:

- Who is the stakeholder?
- What is the observable pain?
- Why is this real? (evidence)
- What is the cost of not solving it?
- What belongs in Out of Scope?

### Step 2 — Validation prompt

Before the agent generates content, validate:

- "This prompt represents what we discussed — does it capture what you want done?"
- Human corrects → identify which D2 pillar was misunderstood
- Human approves → proceed via Task

### Step 3 — Index update prompt

After writing the REQ, ask the agent to update the index file.

---

## Writing an ADR

### Step 1 — Discovery prompt

Ask these questions to scope the decision:

- What architectural problem needs solving?
- What constraints apply?
- Which services are affected?

### Step 2 — Validation prompt

Before the agent generates content, validate:

- "This prompt represents what we discussed — does it capture what you want done?"
- Human corrects → identify which D2 pillar was misunderstood
- Human approves → proceed via Task

### Step 3 — Index update prompt

After writing the ADR, ask the agent to update the index file.

---

## What the AI agent will never do for you

| Task | Why |
|---|---|
| Set `status: accepted` | Requires human product judgment |
| Add yourself to `author` | Human accountability |
| Fill in `deciders` | Must reflect actual decision-makers |
| Decide what goes in Out of Scope | Requires product strategy knowledge |
