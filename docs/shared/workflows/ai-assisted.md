# AI-Assisted Contribution Patterns

> Five patterns for using AI tools productively.

---

Before using AI tools, ensure you have the required extensions and configurations set up:

| Tool | Setup Instructions |
|---|---|
| OpenCode | Follow the project's `.opencode.json` configuration |

---

## Pattern 1: Describe what you want, let the agent do the work

> Best for: Automated tasks with clear acceptance criteria

**Do this when:**
- You know exactly what output you need
- The task has a defined template or checklist
- Little ambiguity in scope

**Example:** "Generate acceptance criterion AC-001 for REQ-F-001."

---

## Pattern 2: Ask the agent to check your work before committing

> Best for: Validation and quality gates

**Do this when:**
- You've drafted content and want validation
- You need a checklist review before committing
- You want to catch issues before spending more work

**Example:** "Check this REQ against guidelines.md §PR Checklist. List all violations."

---

## Pattern 3: Ask the agent to handle git and PR steps

> Best for: Streamlining the Git workflow

**Do this when:**
- You want the agent to create branches
- You want the agent to write commit messages
- You want the agent to open PRs with descriptions

**Example:** "Create a feature branch for REQ-F-001, write tests for AC-001, commit with conventional format, and open a PR."

---

## Pattern 4: Ask the agent to create new content from scratch

> Best for: First drafts of new documents

**Do this when:**
- You have a problem description but no document
- The agent can research the pattern from guidelines
- You want a first draft to iterate on

**Example:** "Create a new REQ for password length validation using the template."

---

## Pattern 5: Ask the agent to fix code or configuration

> Best for: Iterative improvements and bug fixes

**Do this when:**
- There's an existing file to modify
- The fix is well-defined and low-risk
- You want to see proposed changes first

**Example:** "Fix this typo in the problem statement and update the H1 heading to match."
