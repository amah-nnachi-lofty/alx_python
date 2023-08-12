#!/usr/bin/python3

def raise_exception_msg(message=""):
    """Raises a name exception with a custom message."""
    if not isinstance(message, str):
        raise TypeError("Message should be a string")
    
    # Raise a name exception with the provided message
    raise NameError(message)
