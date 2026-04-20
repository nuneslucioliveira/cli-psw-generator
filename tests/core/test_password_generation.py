"""Core password generation tests."""
import pytest
from cli_core.password_generator import generate_password


def test_generate_password_with_default_settings():
    """Test password generation with default settings."""
    password = generate_password()
    
    # Default should be 16 characters
    assert len(password) == 16
    
    # Should contain all character types
    assert any(c.isupper() for c in password)
    assert any(c.islower() for c in password)
    assert any(c.isdigit() for c in password)
    assert any(not c.isalnum() for c in password)


def test_generate_password_with_custom_length():
    """Test password generation with custom length."""
    password = generate_password(length=32)
    
    # Should be exactly the specified length
    assert len(password) == 32


def test_generate_password_with_excluded_special():
    """Test password generation with excluded special characters."""
    password = generate_password(exclude_special=True)
    
    # Should not contain special characters
    assert not any(not c.isalnum() for c in password)
    
    # Should still contain other character types
    assert any(c.isupper() for c in password)
    assert any(c.islower() for c in password)
    assert any(c.isdigit() for c in password)