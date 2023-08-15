#!/usr/bin/python3

"""
This module defines the BaseGeometry class and a metaclass BaseMetaClass.
"""

class BaseMetaClass(type):
    """
    Metaclass that customizes the behavior of the dir() function.
    It excludes the '__init_subclass__' attribute from the result.
    """
    def __dir__(cls):
        """
        Return a list of attributes of the class, excluding '__init_subclass__'.
        """
        return [attr for attr in super().__dir__() if attr != '__init_subclass__']

class BaseGeometry(metaclass=BaseMetaClass):
    """
    Base class for geometry-related classes, using BaseMetaClass metaclass.
    It excludes the '__init_subclass__' attribute from the result of dir().
    """
    def __dir__(cls):
        """
        Return a list of attributes of the class, excluding '__init_subclass__'.
        """
        return [attr for attr in super().__dir__() if attr != '__init_subclass__']
