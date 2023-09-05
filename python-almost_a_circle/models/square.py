#!/usr/bin/python3

"""
This module defines the Square class, a specialized rectangle shape with equal sides.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The Square class represents a square shape.

    Attributes:
        size (int): The size of the square's sides.
        x (int): The x-coordinate of the top-left corner of the square.
        y (int): The y-coordinate of the top-left corner of the square.
        id (int): A unique identifier for the square instance.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square's sides.
            x (int, optional): The x-coordinate of the top-left corner (default: 0).
            y (int, optional): The y-coordinate of the top-left corner (default: 0).
            id (int, optional): A unique identifier for the instance (default: generated).

        Raises:
            TypeError: If size, x, or y are not integers.
            ValueError: If size, x, or y are not greater than or equal to 0.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for wsize
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a custom string representation of the square.

        Returns:
            str: A formatted string representation of the square.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)