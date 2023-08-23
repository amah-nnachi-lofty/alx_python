#!/usr/bin/python3

"""
This module defines the Rectangle class.
"""

from models.base import Base

class Rectangle(Base):
    """
    The Rectangle class represents a rectangle shape.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the top-left corner of the rectangle.
        y (int): The y-coordinate of the top-left corner of the rectangle.
        id (int): A unique identifier for the rectangle instance.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the top-left corner (default: 0).
            y (int, optional): The y-coordinate of the top-left corner (default: 0).
            id (int, optional): A unique identifier for the instance (default: generated).
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Other methods...

    def update(self, *args):
        """
        Updates the attributes of the rectangle instance with the provided arguments.

        Args:
            *args: The arguments in the order: id, width, height, x, y.
        """
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)

    def __str__(self):
        """Returns a custom string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

