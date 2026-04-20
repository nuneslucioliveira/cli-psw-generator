# GitHub Issues Tracking

## One tracking issue per accepted REQ

Each REQ with `status: accepted` gets:

1. **One tracking issue** in the GitHub Issues tracker
2. **Phase responsibilities**:
   - **Plan**: Architect documents related ADRs
   - **Task**: Dev Team creates estimates and subtasks
   - **Implement**: Dev writes code with AC-derived tests
   - **Deliver**: PM confirms production deployment

## Issue labels

| Label | When |
|---|---|
| `req:accepted` | REQ reaches `status: accepted` |
| `adr:pending` | Architect needs to write ADRs (Plan phase) |
| `blocked` | REQ has `blocked-by` field populated |

## Issue milestones

Create GitHub milestones matching the valid values in [`../README.md#milestone`](../README.md#milestone).

## Tracking issue template

```markdown
## Summary

[ REQ-NNN: Title ]

## Related Artifacts

- [REQ](file.md) — original requirement

## Progress

- [ ] **Plan**: Architect documents related ADRs
- [ ] **Task**: Dev Team creates issues and estimates
- [ ] **Implement**: Write tests, code, review, merge
- [ ] **Deliver**: PM confirms production deployment

## Notes

<!-- Additional notes go here -->
```
