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

    @property
    def width(self):
        """Getter method for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method for x-coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x-coordinate."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method for y-coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y-coordinate."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of this rectangle"""
        return (self.__width*self.__height)

    def display(self):
        """
        Displays the Rectangle using the '#' character.
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        '''
        Returns a string representation of the rectangle
        '''
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Updates the attributes of this object with new values passed as arguments to this function
        
        Args:
        *args: Variable length argument list containing attributes in order:
            1st argument: id attribute
            2nd argument: width attribute
            3rd argument: height attribute
            4th argument: x attribute
            5th argument: y attribute

        **kwargs: Variable length keyword argument list containing attribute names and values.    
        """

        attributes = ['id', 'width', 'height', 'x', 'y']

        if args:
            for index, value in enumerate(args):
                if index < len(attributes):
                    setattr(self, attributes[index], value)

        if kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)