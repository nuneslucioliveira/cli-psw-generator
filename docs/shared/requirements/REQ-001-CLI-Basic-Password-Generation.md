---
id: REQ-001
title: "CLI Basic Password Generation"
status: accepted
domain: CLI Arguments & Core Generator
milestone: v1.0
priority: must
author:
  - "Agent: curupira-companion"
---

# REQ-001 — CLI Basic Password Generation

> **Note:** This document was reverse-engineered from the existing `cli-interface` and `core-generator` codebases.

## 1. Problem Statement

### Stakeholder

Power users requiring secure, CLI-based password generation for scripts, automated workflows, and terminal operations.

### Problem

The existing password generation capability lacks a formal specification. Without documented requirements, the system risks security drift, inconsistent behavior, and inadequate test coverage over time.

### Evidence

- Code exists in `cli-interface` and `core-generator` services
- No formal requirements document governing behavior
- Test coverage not verified against documented acceptance criteria

### Cost of Inaction

- Security vulnerabilities from undocumented edge cases
- Inconsistent password generation behavior
- Poor test coverage leading to undetected regressions
- Difficulty onboarding new contributors

## 2. Functional Requirements

### REQ-F-001 — Password Length Configuration

The system SHALL accept a password length parameter via CLI argument. The minimum length SHALL be 8 characters. The maximum length SHALL be 128 characters. Lengths outside this range SHALL result in an error to stderr.

### REQ-F-002 — Character Set Configuration

The system SHALL accept character set configuration via CLI arguments. The system SHALL support the following character sets:

- Uppercase letters (A-Z)
- Lowercase letters (a-z)
- Digits (0-9)
- Special characters (non-alphanumeric)

The system SHALL include at least one character from each selected set when all sets are enabled.

### REQ-F-003 — Stdout Output

The system SHALL output the generated password to stdout. The password SHALL be output as plain text without additional formatting, prefixes, or suffixes.

### REQ-F-004 — Stderr Error Reporting

The system SHALL output error messages to stderr. Error messages SHALL include a description of the failure condition. The system SHALL return a non-zero exit code on error.

### REQ-F-005 — Default Behavior

The system SHALL provide sensible defaults when optional parameters are omitted. The default password length SHALL be 16 characters. By default, the system SHALL include uppercase, lowercase, digits, and special characters.

## 3. Non-Functional Requirements

| ID | Quality Attribute (ISO 25010) | Metric | Target | Condition |
|---|---|---|---|---|
| REQ-001-NFR-001 | Performance Efficiency — Time Behaviour | Time to generate single password | < 100 ms | Password length 8-128 chars, standard hardware |
| REQ-001-NFR-002 | Security — Authenticity | Entropy source | Cryptographically secure PRNG | Password generation uses OS-level CSPRNG |
| REQ-001-NFR-003 | Usability — Operability | CLI argument discovery | < 5 seconds | First-time user identifies required arguments via `--help` |

## 4. Acceptance Criteria

### AC-001 — Default password generation produces valid output

**Given** the user invokes the CLI without arguments,
**When** the command executes successfully,
**Then** a 16-character password is output to stdout containing at least one uppercase letter, one lowercase letter, one digit, and one special character.

### AC-002 — Custom length within range succeeds

**Given** the user specifies a length of 32 characters,
**When** the command executes successfully,
**Then** the output password is exactly 32 characters long.

### AC-003 — Length below minimum fails gracefully

**Given** the user specifies a length of 5 characters,
**When** the command executes,
**Then** an error message is written to stderr and the exit code is non-zero.

### AC-004 — Length above maximum fails gracefully

**Given** the user specifies a length of 200 characters,
**When** the command executes,
**Then** an error message is written to stderr and the exit code is non-zero.

### AC-005 — Character set exclusion excludes specified characters

**Given** the user excludes special characters via CLI argument,
**When** the command executes successfully,
**Then** the output password contains no special characters.

### AC-006 — Password generation completes within time target

**Given** the user invokes the CLI with a length of 64 characters,
**When** the command executes,
**Then** the password is generated and output within 100 milliseconds (p95 over 100 iterations).

## 5. Out of Scope

- Batch password generation (generating multiple passwords in a single invocation)
- Graphical user interface (GUI) or web interface
- Entropy metering or quality visualization
- Third-party integrations (password managers, API services)
- Non-ASCII character sets (emojis, Unicode beyond standard ASCII)
- Password strength scoring or validation against known weak passwords

## 6. Dependencies

### Internal Dependencies

- `cli-interface` service: CLI argument parsing and output handling
- `core-generator` service: Password generation logic

### External Dependencies

- Operating system cryptographically secure pseudo-random number generator (CSPRNG)
- Standard input/output streams (stdin, stdout, stderr)
