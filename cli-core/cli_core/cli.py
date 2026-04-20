"""CLI interface for password generator."""
import argparse
import sys
from .password_generator import generate_password


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Generate cryptographically secure passwords",
        prog="password-generator"
    )
    
    parser.add_argument(
        "--length",
        type=int,
        default=16,
        help="Password length (8-128 characters, default: 16)"
    )
    
    parser.add_argument(
        "--exclude-special",
        action="store_true",
        help="Exclude special characters from password"
    )
    
    parser.add_argument(
        "--exclude-digits",
        action="store_true",
        help="Exclude digits from password"
    )
    
    parser.add_argument(
        "--exclude-lowercase",
        action="store_true",
        help="Exclude lowercase letters from password"
    )
    
    parser.add_argument(
        "--exclude-uppercase",
        action="store_true",
        help="Exclude uppercase letters from password"
    )
    
    args = parser.parse_args()
    
    try:
        password = generate_password(
            length=args.length,
            exclude_special=args.exclude_special,
            exclude_digits=args.exclude_digits,
            exclude_lowercase=args.exclude_lowercase,
            exclude_uppercase=args.exclude_uppercase
        )
        print(password)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()