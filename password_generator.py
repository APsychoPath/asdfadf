#!/usr/bin/env python3
"""
Password Generator
-------------------
A simple script to generate secure random passwords based on user preferences.
"""

import random
import string
import argparse


def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    """
    Generate a random password based on the given criteria.
    
    Args:
        length (int): Length of the password (default: 12)
        use_uppercase (bool): Include uppercase letters (default: True)
        use_digits (bool): Include digits (default: True)
        use_special (bool): Include special characters (default: True)
    
    Returns:
        str: Generated password
    """
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ""
    digits = string.digits if use_digits else ""
    special = "!@#$%^&*()_+-=[]{}|;:,.<>?" if use_special else ""
    
    # Combine all allowed characters
    all_chars = lowercase + uppercase + digits + special
    
    # Validate that at least one character set is enabled
    if not all_chars:
        raise ValueError("At least one character set must be enabled")
    
    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    # Ensure the password meets complexity requirements
    if use_uppercase and not any(c in uppercase for c in password):
        password = password[:-1] + random.choice(uppercase)
    if use_digits and not any(c in digits for c in password):
        password = password[:-1] + random.choice(digits)
    if use_special and not any(c in special for c in password):
        password = password[:-1] + random.choice(special)
    
    return password


def main():
    """
    Main function to handle command-line arguments and generate password.
    """
    parser = argparse.ArgumentParser(description="Generate a secure random password.")
    parser.add_argument("-l", "--length", type=int, default=12, 
                       help="Length of the password (default: 12)")
    parser.add_argument("--no-uppercase", action="store_false", dest="use_uppercase",
                       help="Exclude uppercase letters")
    parser.add_argument("--no-digits", action="store_false", dest="use_digits",
                       help="Exclude digits")
    parser.add_argument("--no-special", action="store_false", dest="use_special",
                       help="Exclude special characters")
    
    args = parser.parse_args()
    
    try:
        password = generate_password(
            length=args.length,
            use_uppercase=args.use_uppercase,
            use_digits=args.use_digits,
            use_special=args.use_special
        )
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()