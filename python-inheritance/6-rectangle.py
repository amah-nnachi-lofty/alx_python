#!/usr/bin/python3

"""
This module defines the Rectangle class based on BaseGeometry.
"""

class BaseGeometry:
    """
    Base class for geometry-related classes.
    """
    def area(self):
        """
        Placeholder for area calculation.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    Rectangle class based on BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

"""
Output: True
"""
print(issubclass(Rectangle, BaseGeometry)) 
