#!/usr/bin/python3

def raise_exception():
    """Raises a type exception."""
    try:
        # Attempt to add incompatible types (string and integer)
        result = 'Hello' + 5  # This will raise a TypeError exception
    except TypeError as e:
        # Catch the TypeError exception
        raise e  # Re-raise the caught exception

