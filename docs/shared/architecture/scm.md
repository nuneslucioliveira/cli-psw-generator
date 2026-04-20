# SCM Rules — Branching Strategy and Workflows

## Who should read what

| Persona | Files to read |
|---|---|
| **Designer** | `architecture/overview.md`, requirements, workflow guides |
| **PM/PO** | `requirements/`, methodology, issue-tracking workflow |
| **Architect** | `architecture/adrs/`, methodology, scm.md |
| **Developer** | `architecture/`, requirements, code-review workflow |

## Branching Strategy

This repository uses **Trunk-based (main only + short-lived feature branches)**.

- **`main`**: The single integration branch for CI/CD
- **Feature branches**: Short-lived branches named `feature/<ticket-id>-<description>`
- **Hotfix branches**: For critical fixes, named `hotfix/<short-description>`
- **PR targeting**: All feature branches merge directly to `main`
- **No long-lived branches**: Avoid `develop` branches in trunk-based workflows

## Pull Request Process

1. **Create a feature branch** from `main` with a descriptive name
2. **Make your changes** and test them locally
3. **Open a PR** targeting `main`
4. **CI builds and tests** automatically — resolve any failures
5. **Human and AI code review** completes the check
6. **Merge to main** — protected branch with required reviews

## PR Description Format

```markdown
## Summary
One-paragraph explanation of what changed and why.

## Key changes
- Bullet points of significant changes
- Links to related REQ or ADR

## Related [REQ/ADR]
- [REQ-NNN](file.md) or [ADR-NNN](file.md)
```

## Code Reviews

- PRs require at least one approving review
- AI-assisted review via `instructions/` files
- All ACs must be verified before merge
- Comments should focus on quality, not style
- Use `squash and merge` for linear history

## Commit Messages

Use **Conventional Commits** format:

```
<type>: <subject>

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `refactor`: Code change that neither fixes nor adds feature
- `chore`: Maintenance, build, auxiliary changes

**Guidelines:**
- Imperative mood: "Add feature" not "Added feature"
- No period at end of subject line
- Limit subject line to 72 characters
- Scope in parentheses if needed: `feat(cli): add password length validation`

## Release Management

- **Versioning**: Semantic versioning (MAJOR.MINOR.PATCH)
- **Release commits**: `chore: release v1.2.3`
- **Tags**: Create git tags for releases
- **Changelog**: Automatically generated from commit history

## Repositories

- **Main repository**: `[PROJECT_NAME]` — CLI Password Generator
  - Contains all documentation (ADRs, REQs, workflows)
  - No application code — documentation-only repository
