# Adding Skills to the AI Stack

## When to Add a Skill

Add a new skill when:

- A recurring task pattern emerges that needs special handling
- A new domain requires specialized knowledge
- An existing skill shows gaps that warrant extension

## How to Add a Skill

1. **Create the skill directory** in `.opencode/skills/<skill-name>/`
2. **Write the YAML frontmatter** with name and description
3. **Document the skill's responsibilities** and constraints
4. **Reference existing skills** where appropriate (don't duplicate)
5. **Link from workflows-index.md** to route situations to the skill

## Skill Structure

Each skill should have these core files:

| File | Purpose |
|---|---|
| SKILL.md | Skill descriptor with frontmatter and responsibilities |
| domain-specific.md | Domain logic for the skill's specialty |
| hard-stops.md | Prohibited actions for this skill |
| workflows-index.md | Routing map for contributor tasks |

## Validation Checklist

Before committing a new skill:

- [ ] Name follows project conventions
- [ ] Skills directory exists at `.opencode/skills/<skill-name>/`
- [ ] SKILL.md has YAML frontmatter with name and description
- [ ] Skill declares its read-only nature if applicable
- [ ] Hard-stops document what the skill cannot do
- [ ] Workflows-index.md is updated with new routing entries
- [ ] Skill references existing skills for cross-references

## Example Skill Entry

In your SKILL.md:

```yaml
---
name: <skill-name>
description: <What this skill does>
---
```

## References

- Core companion skill: `.opencode/skills/curupira-companion/SKILL.md`
- Workflows index: `.opencode/skills/curupira-companion/workflows-index.md`
- SDD methodology: `docs/shared/methodology.md`
