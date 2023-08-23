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

    # ... (rest of the class remains the same)

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle instance with provided arguments.

        Args:
            args: A variable number of no-keyword arguments to update the attributes.
                  The order of arguments should be: [id, width, height, x, y].
            kwargs: Keyword arguments to update the attributes.
                    Attributes are updated based on key/value pairs.

        Note:
            If both no-keyword arguments and keyword arguments are provided,
            the no-keyword arguments take precedence in updating the attributes.
        """
        if args and len(args) > 0:
            self.id = args[0]
        if args and len(args) > 1:
            self.width = args[1]
        if args and len(args) > 2:
            self.height = args[2]
        if args and len(args) > 3:
            self.x = args[3]
        if args and len(args) > 4:
            self.y = args[4]
        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Returns a custom string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)