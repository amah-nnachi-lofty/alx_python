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
        if not isinstance(size, int) or size <= 0:
            raise ValueError("size must be a positive integer")
        if size <= 0:
            raise ValueError("size must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        super().__init__(size, size, x, y, id)


    def __str__(self):
        """
        Returns a custom string representation of the square.

        Returns:
            str: A formatted string representation of the square.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the square instance with the provided arguments.

        Args:
            *args: The positional arguments in the order: id, size, x, y.
            **kwargs: The keyword arguments to update specific attributes.
        """
        super().update(*args, **kwargs)

        # The `size` attribute takes precedence over the `width` attribute.
        if "size" in kwargs and isinstance(kwargs["size"], int):
            self.width = self.height = kwargs["size"]


    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.width * self.width

    def display(self):
        """
        Displays the square using '#' characters.

        Prints the square's representation with appropriate adjustments for coordinates.
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)
