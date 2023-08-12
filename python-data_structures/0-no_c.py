#!/usr/bin/env python3

def no_c(my_string):
    """Removes all occurrences of 'c' and 'C' from the input string."""
    
    # Initialize an empty string to store the modified string
    new_string = ""
    
    # Iterate through each character in the input string
    for char in my_string:
        # Check if the character is not 'c' or 'C'
        if char != 'c' and char != 'C':
            # Append the character to the new string
            new_string += char
            
    # Return the modified string without 'c' and 'C'
    return new_string
