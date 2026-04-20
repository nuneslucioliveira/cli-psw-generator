# Small Changes: Quick Correction Workflow

> For typos, wording, status updates, and minor corrections.

---

## Path A: You have a local clone

For Designers, PMs, and anyone with repo access:

1. **Switch to a new branch**
   ```bash
   git checkout -b fix/tiny-correction
   ```

2. **Edit the file**
   Update the typo, wording, or status you want to change.

3. **Commit your change**
   ```bash
   git commit -m "docs: fix typo/status in REQ-NNN"
   ```

4. **Open a PR**
   Target `main` with a description referencing the specific change.

---

## Path B: Via submodule (Developers/Architects)

If the shared-docs is a submodule in your microservice repo:

1. **Switch to a new branch**
   ```bash
   git checkout -b fix/tiny-correction
   ```

2. **Edit the file**
   Update the typo, wording, or status you want to change in the submodule.

3. **Commit your change**
   ```bash
   git add ./docs/shared/path/to/file
   git commit -m "docs: fix tiny correction in shared docs"
   ```

4. **Open a PR**
   Target `main` with a description referencing the specific change.

---

## After merging

- Index files must be updated in the same PR (if you modified or created files).
- If `status: accepted`, verify zero `TBD`/`TO-DO` in the body.
