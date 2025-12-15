#!/usr/bin/env python3
"""
Test script for the password generator.
"""

from password_generator import generate_password

# Test 1: Default settings
print("Test 1 - Default settings:")
print(generate_password())
print()

# Test 2: Custom length
print("Test 2 - Custom length (20):")
print(generate_password(length=20))
print()

# Test 3: No special characters
print("Test 3 - No special characters:")
print(generate_password(use_special=False))
print()

# Test 4: Only lowercase and digits
print("Test 4 - Only lowercase and digits:")
print(generate_password(use_uppercase=False, use_special=False))
print()

# Test 5: Only lowercase letters (minimum complexity)
print("Test 5 - Only lowercase letters (minimum complexity):")
print(generate_password(use_uppercase=False, use_digits=False, use_special=False))
print()

# Test 6: Demonstrate error handling (this would require modifying the function)
print("Test 6 - Error handling demonstration:")
print("Note: The function always includes lowercase letters, so it won't raise an error.")
print("To see the error, you would need to modify the function to allow disabling lowercase.")