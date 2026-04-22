"""BDD tests for character set exclusion - AC-005."""

import pytest
import re


def test_character_set_exclusion_excludes_specified_characters(cli_runner):
    """AC-005: Character set exclusion excludes specified characters."""
    # Given the user excludes special characters via CLI argument
    result = cli_runner(["--exclude-special"])

    # When the command executes successfully
    assert result.returncode == 0
    assert result.stderr == ""

    # Then the output password contains no special characters
    password = result.stdout.strip()

    # Check that password contains no special characters (non-alphanumeric)
    assert not re.search(r"[^A-Za-z0-9]", password)

    # Check that it still contains other character types
    assert re.search(r"[A-Z]", password)  # uppercase letters
    assert re.search(r"[a-z]", password)  # lowercase letters
    assert re.search(r"\d", password)  # digits
