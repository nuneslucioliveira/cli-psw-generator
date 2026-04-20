# Shared Documentation

CLI Password Generator shared documentation for the SDD lifecycle.

This scaffold applies Spec Driven Development to a command-line tool that generates secure, customizable passwords based on user-defined length and character set constraints. The specification is the authoritative source of truth, and implementation only begins when the spec is stable and approved.

## Structure

| Directory | Contents |
|---|---|
| `architecture/` | System overview, tech stack, glossary, SCM rules, ADRs |
| `requirements/` | Product requirements (REQs) |
| `workflows/` | Step-by-step contribution guides |
| `methodology.md` | SDD lifecycle, vocabulary reference, and evaluation criteria |

## Authoring Guidelines

- **Writing REQs and ADRs:** [`requirements/guidelines.md`](../requirements/guidelines.md) and [`architecture/adrs/guidelines.md`](../architecture/adrs/guidelines.md)
- **Templates:** [`requirements/000-template.md`](../requirements/000-template.md) and [`architecture/adrs/000-template.md`](../architecture/adrs/000-template.md)

## Milestone

| Value | Meaning |
|---|---|
| mvp | Basic generation of alphanumeric passwords of a specified length |
| v2 | Support for special characters, exclusion rules, and CLI flags |

## How to Contribute

Start with [`workflows/README.md`](workflows/README.md) to find your workflow and follow the step-by-step guides.
