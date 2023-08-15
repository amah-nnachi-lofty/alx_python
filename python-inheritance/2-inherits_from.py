#!/usr/bin/python3

"""
Module: 2-inherits_from
Contains the function `inherits_from` which checks if an object is an instance of a class
that inherited (directly or indirectly) from the specified class.
"""

def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited (directly or indirectly)
    from the specified class.

    Args:
        obj (object): The object to be checked.
        a_class (type): The class to compare against.

    Returns:
        bool: True if the object's class is a subclass of the specified class, otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
