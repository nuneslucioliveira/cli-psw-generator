# Code Review Instructions

This repository contains only documentation (ADRs and REQs). No application code.
Apply the checks below to every pull request.

---

## PR Blockers — Hard Stops

Flag as a blocker (must be fixed before merging):

- Any document with `status: accepted`, `implemented`, or `delivered` that contains
  `TBD`, `TO-DO`, or `[to be defined]` anywhere in the body.
- Any new or modified ADR/REQ that is **not listed** in its corresponding index file
  in the same PR.
- Any ADR missing a mandatory frontmatter field: `id`, `title`, `status`, `service`, `milestone`, `date`, `deciders`.
- Any REQ missing a mandatory frontmatter field: `id`, `title`, `status`, `domain`,
  `milestone`, `priority`, `author`.
- Any REQ `milestone` field containing a value outside the valid set defined in `README.md § Milestone`.

---

## Commit and PR Format

- Commit messages must follow Conventional Commits: `docs:`, `feat:`, `fix:`, `chore:`, etc.
- PR description must include a **Summary** section and a **Key changes** section.
- PR must target `main`. Flag if the target branch is anything other than `main`.

---

## Index File Maintenance

- Every ADR must appear in exactly one `architecture/adrs/index-<service>.md`.
- Every REQ must appear in exactly one `requirements/index-<domain>.md`.
- The index entry must be added or updated in the same PR as the document change.

---

## Cross-Reference Integrity

- `related-adrs` entries in a REQ should reference IDs that exist in the ADR corpus.
- `requires` entries in a REQ should reference IDs that exist in the REQ corpus.
- `related-reqs` entries in an ADR should reference IDs that exist in the REQ corpus.
- Flag any reference to an ID that does not appear in any index file.
