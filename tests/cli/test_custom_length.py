"""BDD tests for custom length password generation - AC-002."""

import pytest


def test_custom_length_within_range_succeeds(cli_runner):
    """AC-002: Custom length within range succeeds."""
    # Given the user specifies a length of 32 characters
    result = cli_runner(["--length", "32"])

    # When the command executes successfully
    assert result.returncode == 0
    assert result.stderr == ""

    # Then the output password is exactly 32 characters long
    password = result.stdout.strip()
    assert len(password) == 32
