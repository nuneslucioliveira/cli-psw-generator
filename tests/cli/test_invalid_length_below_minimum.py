"""BDD tests for invalid length below minimum - AC-003."""

import pytest


def test_length_below_minimum_fails_gracefully(cli_runner):
    """AC-003: Length below minimum fails gracefully."""
    # Given the user specifies a length of 5 characters
    result = cli_runner(["--length", "5"])

    # When the command executes
    # Then an error message is written to stderr and the exit code is non-zero
    assert result.returncode != 0
    assert result.stderr != ""
