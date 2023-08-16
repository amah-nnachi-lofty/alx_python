#!/usr/bin/python3

"""
This module defines the BaseGeometry class and a metaclass BaseMetaClass.
"""

class BaseGeometry(metaclass=BaseMetaClass):
    """
    Base class for geometry-related classes, using BaseMetaClass metaclass.
    It excludes the '__init_subclass__' attribute from the result of dir().
    """
    def __dir__(self):
        """
        Return a list of attributes of the class, excluding '__init_subclass__'.
        """
        return [attr for attr in super().__dir__() if attr != '__init_subclass__']

    def area(self):
        """
        Public instance method that raises an Exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value to be an integer and greater than 0.
        Args:
            name (str): Name of the value being validated.
            value (int): Value to be validated.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialize the Rectangle with width and height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

class Square(Rectangle):
    """
    Square class that inherits directly from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize the Square with size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Return a string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """
        Calculate the area of the square.
        """
        return self.__size ** 2
