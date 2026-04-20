"""BDD tests for default password generation - AC-001."""
import pytest
import re


def test_default_password_generation_produces_valid_output(cli_runner):
    """AC-001: Default password generation produces valid output."""
    # Given the user invokes the CLI without arguments
    result = cli_runner([])
    
    # When the command executes successfully
    assert result.returncode == 0
    assert result.stderr == ""
    
    # Then a 16-character password is output to stdout containing 
    # at least one uppercase letter, one lowercase letter, one digit, and one special character
    password = result.stdout.strip()
    
    # Check password is 16 characters long
    assert len(password) == 16
    
    # Check contains at least one uppercase letter
    assert re.search(r'[A-Z]', password)
    
    # Check contains at least one lowercase letter
    assert re.search(r'[a-z]', password)
    
    # Check contains at least one digit
    assert re.search(r'\d', password)
    
    # Check contains at least one special character
    assert re.search(r'[^A-Za-z0-9]', password)