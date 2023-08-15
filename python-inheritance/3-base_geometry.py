#!/usr/bin/python3
"""3-base_geometry module

This module contains the definition of the BaseGeometry class.
"""

class BaseGeometry:
    """BaseGeometry class

    An empty class that defines the base geometry.
    """
    def __dir__(self):
        """Return the list of attributes and methods of the object"""
        return []

if __name__ == "__main__":
    """Testing the BaseGeometry class"""
    print(dir(BaseGeometry))
    bg = BaseGeometry()
    print(dir(bg))
