"""Core password generation logic."""
import secrets
import string
from typing import Optional


def generate_password(
    length: int = 16,
    exclude_special: bool = False,
    exclude_digits: bool = False,
    exclude_lowercase: bool = False,
    exclude_uppercase: bool = False
) -> str:
    """
    Generate a cryptographically secure password.
    
    Args:
        length: Password length (8-128 characters)
        exclude_special: Whether to exclude special characters
        exclude_digits: Whether to exclude digits
        exclude_lowercase: Whether to exclude lowercase letters
        exclude_uppercase: Whether to exclude uppercase letters
        
    Returns:
        Generated password string
        
    Raises:
        ValueError: If length is outside valid range (8-128)
    """
    # Validate length
    if length < 8 or length > 128:
        raise ValueError("Password length must be between 8 and 128 characters")
    
    # Build character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Remove excluded character sets
    chars = ""
    required_chars = []
    
    if not exclude_uppercase:
        chars += uppercase
        required_chars.append(secrets.choice(uppercase))
    
    if not exclude_lowercase:
        chars += lowercase
        required_chars.append(secrets.choice(lowercase))
    
    if not exclude_digits:
        chars += digits
        required_chars.append(secrets.choice(digits))
    
    if not exclude_special:
        chars += special
        required_chars.append(secrets.choice(special))
    
    # If no character sets are selected, raise an error
    if not chars:
        raise ValueError("At least one character set must be included")
    
    # Generate password
    password_chars = required_chars + [secrets.choice(chars) for _ in range(length - len(required_chars))]
    
    # Shuffle the password characters
    secrets.SystemRandom().shuffle(password_chars)
    
    return "".join(password_chars)