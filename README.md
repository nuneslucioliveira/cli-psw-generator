# CLI Password Generator

Implementation of REQ-001: CLI Basic Password Generation

## Implementation Status

All acceptance criteria from REQ-001 have been implemented and tested:

- AC-001: Default password generation produces valid output ✓
- AC-002: Custom length within range succeeds ✓
- AC-003: Length below minimum fails gracefully ✓
- AC-004: Length above maximum fails gracefully ✓
- AC-005: Character set exclusion excludes specified characters ✓
- AC-006: Password generation completes within time target ✓

## Structure

```
.
├── cli-core/                  # Core implementation package
│   ├── cli_core/              # Python package
│   │   ├── __init__.py
│   │   ├── cli.py             # CLI interface
│   │   └── password_generator.py # Core logic
│   ├── setup.py
│   ├── requirements.txt
│   └── README.md
└── tests/                     # Test suite
    ├── conftest.py
    ├── cli/
    │   ├── test_default_generation.py
    │   ├── test_custom_length.py
    │   ├── test_invalid_length_below_minimum.py
    │   ├── test_invalid_length_above_maximum.py
    │   ├── test_character_exclusion.py
    │   └── test_performance.py
    └── core/
        └── test_password_generation.py
```

## Installation & Usage

1. Navigate to cli-core directory:
   ```bash
   cd cli-core
   ```

2. Create and activate virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the package in development mode:
   ```bash
   pip install -e .
   ```

4. Install testing dependencies:
   ```bash
   pip install pytest
   ```

5. Run tests:
   ```bash
   pytest tests/
   ```

## Features

- Cryptographically secure password generation using `secrets` module
- Configurable password length from 8 to 128 characters
- Configurable character set inclusion (upper, lower, digits, special)
- Default behavior with all character sets included (16 characters)
- Proper error handling with informative messages to stderr
- Performance optimized to generate passwords well under 100ms