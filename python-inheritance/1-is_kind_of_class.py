#!/usr/bin/python3

"""
Module to check if an object is an instance of, or if the object's class inherited from, the specified class.
"""

def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if the object's class inherited from, the specified class.

    Args:
        obj (object): The object to be checked.
        a_class (type): The class to compare against.

    Returns:
        bool: True if the object's class is the specified class or a subclass of it, otherwise False.
    """
    return isinstance(obj, a_class)
