# GitHub Actions Secrets Configuration Guide

## Purpose

This document describes how to configure GitHub Actions secrets required for the PyPI package upload workflow (ADR-002).

---

## Required Secrets

### `PYPI_API_TOKEN`

**Description:** PyPI API token with upload permissions for the `cli-password-generator` package.

**Type:** PyPI API Token (not username/password)

**Scope:** Repository-level, accessible only to maintainers

**Rotation:** Rotate per security policy or credential compromise

---

## Creating the PyPI API Token

### Option A: Personal Access Token (Recommended)

1. Go to https://pypi.org/account/
2. Click on "Add token" or "Generate a new token"
3. Give it a descriptive name (e.g., `CLI Password Generator Upload`)
4. Set scopes to "Full Project" or at least "Write" permissions
5. Copy and save the token (you won't see it again)
6. Add it as a GitHub Actions secret:
   ```bash
   echo "PYPI_API_TOKEN=$TOKEN" >> github-actions-secrets.env
   ```
7. Set the secret in your repository's Actions settings

### Option B: Two-Factor Authentication Compatible Token (Most Secure)

1. Enable 2FA on your PyPI account first
2. Go to https://pypi.org/account/
3. Generate a token with "Write" permissions only
4. Follow the same steps as Option A

---

## GitHub Actions Secret Configuration

### Via GitHub UI

1. Navigate to your repository on GitHub
2. Go to **Settings** → **Secrets and variables** → **Actions**
3. Click **"New repository secret"**
4. **Name:** `PYPI_API_TOKEN`
5. **Secret:** Paste your PyPI token
6. **Description:** PyPI upload token for cli-password-generator package
7. Click **"Add secret"**

### Via GitHub CLI

```bash
gh secret add PYPI_API_TOKEN --body "PyPI upload token"
```

### Via Environment File

For local testing or development environments, use environment files:

```bash
# Create .github/secrets.env
echo "PYPI_API_TOKEN=$TOKEN" > .github/secrets.env
```

Reference this file in CI/CD documentation or local build pipelines.

---

## Workflow Integration

The token is referenced in `.github/workflows/release.yml`:

```yaml
publish:
  with:
    password: ${{ secrets.PYPI_API_TOKEN }}
```

---

## Security Best Practices

1. **Don't commit tokens to your repository**
2. **Use repository-level secrets** (not organization-wide unless necessary)
3. **Rotate tokens regularly** per your security policy
4. **Monitor token usage** in GitHub Actions logs
5. **Remove deprecated tokens** and generate new ones
6. **Use separate tokens** for different environments (development, staging, production)

---

## Reference

- [PyPI API Token Documentation](https://pypi.org/help/#apitoken)
- [PyPI Token Scopes](https://pypi.org/help/#apitoken)
- [GitHub Actions Secrets Guide](https://docs.github.com/actions/security/understanding-and-configuring-secrets)

---

## Related Artifacts

- ADR-002: CI/CD Deployment Strategy for CLI Password Generator
- MADR-001: Distinguishing Implemented from Delivered Status
- .github/workflows/release.yml

(End of file - total 58 lines)