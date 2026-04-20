---
id: ADR-001
title: Use Python standard library for cryptographic password generation
status: accepted
service: platform
milestone: v1.0
date: 2026-04-20
deciders:
  - "Agent: curupira-companion"
  - "@nuneslucioliveira"
  - "nuneslucioliveira"
---

# ADR-001: Use Python standard library for cryptographic password generation

> **Note:** This ADR was reverse-engineered from the existing `core-generator` codebase. It formalises a decision already present in the implementation.

## Context and Problem Statement

REQ-001 requires secure password generation for command-line use. The decision to document now captures the architectural choices already embedded in the implementation for future maintainability and audit purposes.

**Quality Attribute Drivers:**

- **Security (ISO 25010: Security — Confidentiality):** Passwords must be cryptographically non-predictable and resistant to entropy-based attacks
- **Usability (ISO 25010: Usability — Operability):** CLI interface must be simple, requiring no external dependencies or configuration

**Problem:** The CLI Password Generator requires a reliable, secure source of randomness for password generation while maintaining a minimal dependency surface.

## Considered Options

1. **Python `secrets` and `random.SystemRandom` modules** — Standard library CSPRNG based on OS entropy sources (`/dev/urandom` on Unix, `CryptGenRandom` on Windows)
2. **External crypto library (e.g., `cryptography`, `passlib`)** — Third-party packages with dedicated cryptographic primitives
3. **Entropy-based generation from `/dev/random` directly** — Blocking entropy source for maximum security guarantee

## Decision Outcome

Chosen option: **"Python `secrets` and `random.SystemRandom` modules"**, because it provides cryptographically secure randomness with zero external dependencies.

### Consequences

Good, because: No external dependencies reduces attack surface, supply chain risk, and deployment complexity

Good, because: Standard library modules are maintained by Python core team with long-term stability guarantees

Bad, because: Limited to ASCII character sets only — mitigated/acceptable: Non-ASCII password support is explicitly out-of-scope per REQ-001 constraints

Bad, because: No built-in password strength scoring — mitigated/acceptable: Out-of-scope for v1.0; can be added as post-generation validation in future ADR

Neutral, because: Performance is negligible for password generation workloads — this is not a high-throughput service

### Implementation Notes

**Character Set Management Pattern:**

The core generator separates character set composition into discrete subsets (uppercase, lowercase, digits, symbols) to ensure at least one character from each selected subset is included in the generated password.

**Length Validation Boundaries:**

- Minimum length: 8 characters (security baseline)
- Maximum length: 128 characters (practical CLI output limit)
- Validation occurs at CLI argument parsing layer before generation

**CSPRNG Usage:**

```mermaid
graph LR
    A[CLI Argument] --> B[Validation Layer]
    B --> C[Character Set Composition]
    C --> D[random.SystemRandom]
    D --> E[/dev/urandom]
    D --> F[OS Entropy Source]
    E --> G[Password Output]
    F --> G
```

## Sources

- This decision was reverse-engineered from the existing `core-generator` codebase which uses `random.SystemRandom` for entropy sourcing and `secrets` module for character selection.

-