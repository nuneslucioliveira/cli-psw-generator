---
applyTo: "requirements/REQ-*.md"
---

- Dependencies must not list ADR IDs — use `related-adrs` frontmatter instead.
- Out of Scope must contain only behavioural descoping — no library, technology, or deployment choices.
- Policy constraints (what the system SHALL NOT do) belong in Problem Statement, not scattered across functional requirements.
- NFRs when present must use five-column table: `ID | Quality Attribute (ISO 25010) | Metric | Target | Condition`.

**Frontmatter — valid values:**

- `status`: `draft` | `accepted` | `implemented` | `delivered` | `cancelled` | `superseded`
- `domain`: cli-arguments | password-logic | security-validation
- `milestone`: mvp | v2
- `priority`: `must` | `should` | `could` | `wont`
- Flag `status: reviewed` or `status: approved` — these are not valid values.

**Structure checks:**

- H1 format must be `# REQ-NNN — Title` (em-dash separator, not colon).
- Every `REQ-F-NNN` has at least one AC.
- `author` field is append-only — flag if existing author entries were removed.
- `SHALL`, `SHOULD`, and `MAY` keywords must be capitalized. Flag lowercase usage.
- REQs must not name specific technologies. Requirements describe observable behavior.
- IDs (`REQ-F-NNN`, `AC-NNN`) must not be renumbered. Gaps are valid.
- NFRs (when present) must name an ISO 25010 subcategory. The absence of an NFR section is NOT a flag.
- Additional sections (Success Metrics, Risks, Proposed Solution) are optional. Do NOT flag their absence.
- Required sections must appear in order: Problem Statement → Functional Requirements → Non-Functional Requirements → Acceptance Criteria → Out of Scope → Dependencies.
- Flag if two FRs describe the same behaviour from opposite angles.
- Flag if an NFR restates what the system does or repeats a policy constraint.
