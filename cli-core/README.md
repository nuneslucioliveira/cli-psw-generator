# CLI Password Generator

A cryptographically secure password generator with CLI interface.

## Installation

```bash
pip install -e .
```

## Usage

### Basic Usage
```bash
password-generator
```

### With Custom Length
```bash
password-generator --length 32
```

### Exclude Character Sets
```bash
password-generator --exclude-special
password-generator --exclude-digits
password-generator --exclude-lowercase
password-generator --exclude-uppercase
```

## Running Tests

```bash
cd /path/to/cli-core
source venv/bin/activate
pip install pytest
pytest tests/
```

## Features

- Cryptographically secure password generation using `secrets` module
- Configurable password length (8-128 characters)
- Configurable character sets
- Default behavior with all character sets included
- Proper error handling with informative messages