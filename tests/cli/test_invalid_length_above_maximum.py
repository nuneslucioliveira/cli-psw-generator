"""BDD tests for invalid length above maximum - AC-004."""
import pytest


def test_length_above_maximum_fails_gracefully(cli_runner):
    """AC-004: Length above maximum fails gracefully."""
    # Given the user specifies a length of 200 characters
    result = cli_runner(["--length", "200"])
    
    # When the command executes
    # Then an error message is written to stderr and the exit code is non-zero
    assert result.returncode != 0
    assert result.stderr != ""