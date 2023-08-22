

"""
This module defines the Base class that provides a basic structure for other classes.
"""

class Base:
    """
    The Base class serves as a foundation for other classes.

    Attributes:
        __nb_objects (int): A private class attribute that keeps track of the number of instances created.
        id (int): A public instance attribute that stores the unique identifier of an instance.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int, optional): An optional integer identifier for the instance.
                If not provided, the instance is assigned a unique identifier based on __nb_objects.
        """
        if id is not None:
            """ Assign provided id to instance attribute id """
            self.id = id  
        else:
            """ Increment __nb_objects """
            Base.__nb_objects += 1  
            """ Assign new value to instance attribute id """
            self.id = Base.__nb_objects  
