#!/usr/bin/python3

def raise_exception_msg(message=""):
    """Raises a name exception with a custom message."""
    
    # Check if the message is not a string using isinstance()
    if not isinstance(message, str):
        # If message is not a string, raise a TypeError with an explanatory message
        raise TypeError("Message should be a string")
    
    # Raise a name exception with the provided message
    raise NameError(message)

