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

    def __str__(self):
        """Returns a custom string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
    
    def update(self, *args, **kwargs):
        """Updates the attributes of this object with new values passed as arguments to this function
        
        Thus, Updates the attributes of the rectangle instance with provided arguments.
        Args:
        *args: Variable length argument list containing attributes in order:
            - 1st argument: id attribute
            - 2nd argument: width attribute
            - 3rd argument: height attribute
            - 4th argument: x attribute
            - 5th argument: y attribute
        **kwargs: Variable length keyword argument list containing attribute names and values.    

        Note:
            If both no-keyword arguments and keyword arguments are provided,
            the no-keyword arguments take precedence in updating the attributes.
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

if __name__ == "__main__":
    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(height=1)
    print(r1)

    r1.update(width=1, x=2)
    print(r1)

    r1.update(y=1, width=2, x=3, id=89)
    print(r1)

    r1.update(x=1, height=2, y=3, width=4)
    print(r1)
