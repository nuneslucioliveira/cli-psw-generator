# CLI Core Service — Agent Instructions

## Service Overview

The `cli-core` service is the pure logic component of the CLI Password Generator. It provides cryptographically secure password generation and validation without any terminal I/O dependencies.

**Purpose:** Pure logic for password generation (randomization + validation)

**Interface:** Called by `cli-interface` with validated arguments, returns password strings

**Stack:** Python stdlib only (`secrets`, `random`, `string`, `argparse`)

**Security:** OS-level CSPRNG via `/dev/urandom` on Unix systems

**Statelessness:** No persistence, no database, pure functions

## Architecture and Boundaries

### Service Boundaries

| Aspect | Boundary |
|---|-|
| Input | Validated arguments from `cli-interface` |
| Output | Password string (no formatting) |
| Dependencies | Python stdlib only |
| Persistence | None (stateless) |
| External Calls | OS entropy source only |

### Module Organization

```mermaid
graph TB
    A[cli-interface] -->|Validated args| B[cli.py]
    B --> C[generate_password]
    C --> D[Character Set Composition]
    D --> E[secrets.SystemRandom]
    E --> F[/dev/urandom]
    F --> G[Password Output]
    G --> H[cli-interface]
```

### Files

| File | Responsibility |
|---|-|
| `cli_core/password_generator.py` | Core password generation logic |
| `cli_core/cli.py` | CLI entry point and argument parsing |
| `cli_core/__init__.py` | Package initialization |
| `tests/test_password_generator.py` | Unit tests for generation logic |
| `tests/test_cli.py` | Integration tests for CLI interface |

## Commands and Official References

### Development Commands

| Operation | Command |
|---|-|
| Install package | `pip install -e .` |
| Run tests | `pytest tests/` |
| Run with coverage | `pytest --cov=cli_core tests/` |
| Execute CLI | `password-generator` |
| Execute with args | `password-generator --length 32 --exclude-special` |

### Official Command Source

All command documentation is maintained in `cli-core/README.md`. Reference that file for:
- Installation procedures
- Usage examples
- Test execution patterns

## Coding Conventions

### Module Requirements

- **Zero external dependencies** beyond Python stdlib
- **Type hints** on all function signatures
- **Docstrings** on all public functions (Args, Returns, Raises)
- **No side effects** in generation logic

### Security Patterns

1. **CSPRNG Usage**
   - Use `secrets.choice()` for character selection
   - Use `secrets.SystemRandom()` for shuffling
   - Never use `random.choice()` for password generation

2. **Character Set Management**
   - Separate character sets into discrete subsets
   - Ensure at least one character from each selected set
   - Shuffle required characters into final password

3. **Validation**
   - Length bounds: 8-128 characters
   - Raise `ValueError` for invalid inputs
   - Validate before generation, fail fast

### Error Handling

| Error Type | Condition |
|---|-|
| `ValueError` | Length outside 8-128 range |
| `ValueError` | All character sets excluded |
| No exception | Valid inputs (no entropy errors expected) |

### Testing Patterns

- **Unit tests:** All functions covered in `test_password_generator.py`
- **Integration tests:** CLI subprocess testing in `test_cli.py`
- **Fixtures:** Use pytest fixtures for test data
- **Coverage target:** 100% on core logic

## Quality Rules

### Performance

| Metric | Target |
|---|-|
| Generation time | < 100ms per password |
| Memory footprint | < 1MB |
| Start time | < 50ms (CLI invocation) |

### Security

| Requirement | Implementation |
|---|-|
| Entropy source | `secrets` module (OS CSPRNG) |
| Character diversity | At least one from each enabled set |
| Length validation | Strict bounds checking |
| No predictability | True random selection |

### Maintainability

- Single responsibility per function
- Clear separation of concerns (CLI vs logic)
- Comprehensive docstrings
- Full test coverage

## Integration Points

### Upstream

- Receives validated arguments from `cli-interface`

### Downstream

- Returns password strings to `cli-interface` for output
- No downstream dependencies

### External

- OS entropy source (`/dev/urandom`)
- Python runtime
- No network calls, no file I/O

## Decision Records

See: `../docs/shared/architecture/adrs/`

## Current State

**Version:** v1.0  
**Status:** Implemented  
**Last Updated:** 2026-04-20  
**Next Review:** Post-v1.0 (feature additions)
