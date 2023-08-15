#!/usr/bin/python3

class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with the given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
