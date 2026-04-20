"""Pytest fixtures for CLI password generator tests."""
import pytest
import subprocess
import sys
from pathlib import Path


@pytest.fixture
def cli_runner():
    """Fixture to run CLI commands."""
    def run_command(args):
        # Use the installed CLI directly
        result = subprocess.run(
            [sys.executable, "-m", "cli_core.cli", *args],
            capture_output=True,
            text=True
        )
        return result
    return run_command


@pytest.fixture
def valid_length_args():
    """Fixture for valid length arguments."""
    return ["--length", "32"]


@pytest.fixture
def invalid_length_args():
    """Fixture for invalid length arguments."""
    return ["--length", "5"]


@pytest.fixture
def exclude_special_args():
    """Fixture for excluding special characters."""
    return ["--exclude-special"]


@pytest.fixture
def default_args():
    """Fixture for default arguments."""
    return []