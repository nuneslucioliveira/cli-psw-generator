# Code Review Checklist

> Review checklist for Pull Requests.

---

## Persona-specific checklists

### Designer

- [ ] Copy and UX language match design system
- [ ] REQ problem statement is clear and specific
- [ ] No technology names in functional requirements
- [ ] Out of Scope contains only behavioural descoping

### PM/PO

- [ ] Product alignment: REQ solves a real problem
- [ ] ACs are complete and testable
- [ ] Status transitions follow the lifecycle
- [ ] Milestone assignment is correct

### Architect

- [ ] ADR consistency with existing decisions
- [ ] Cross-service implications documented
- [ ] Related ADRs link to originating REQs
- [ ] No technology decisions in REQ body

### Developer

- [ ] Code quality standards met
- [ ] AC coverage verified in tests
- [ ] No TBDs/TO-DOs in accepted documents
- [ ] PR follows conventional commits format

---

## AC coverage reminder

> No PR is mergeable without passing tests covering every AC.
