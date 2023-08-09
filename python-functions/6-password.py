#!/usr/bin/python3

def validate_password(password):
    # Check password length
    if len(password) < 8:
        return False
    
    # Check for uppercase, lowercase, and digit characters
    has_upper = False
    has_lower = False
    has_digit = False
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        
        # If all required characters are found, exit the loop early
        if has_upper and has_lower and has_digit:
            break
    
    # Check for spaces
    if ' ' in password:
        return False
    
    # Check if all checks passed
    return has_upper and has_lower and has_digit