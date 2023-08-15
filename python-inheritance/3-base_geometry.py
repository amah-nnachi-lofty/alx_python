"""Module for BaseGeometry class.

This module defines the BaseGeometry class and its metaclass.

The BaseGeometry class is an abstract base class for geometric objects.
It cannot be instantiated directly.
"""


class BaseMetaClass(type):
    """Metaclass for BaseGeometry class.

    This metaclass defines a custom `__dir__` method for the BaseGeometry class
    that returns all attributes of the class except `__init_subclass__`.

    Returns:
        A list of attributes of the class.
    """

    def __dir__(cls):
        """Return all attributes of the class except `__init_subclass__`.

        Args:
            cls: The class to get the attributes for.

        Returns:
            A list of attributes of the class.
        """
        return [attribute for attribute in super().__dir__(cls) if attribute != '__init_subclass__']


class BaseGeometry(metaclass=BaseMetaClass):
    """Abstract base class for geometric objects.

    Args:
        metaclass: The metaclass for the class.

    Raises:
        TypeError: If the class is instantiated.
    """

    def __init__(self):
        raise TypeError("Cannot instantiate abstract base class.")

    def __dir__(cls):
        """Return all attributes of the class except `__init_subclass__`.

        Args:
            cls: The class to get the attributes for.

        Returns:
            A list of attributes of the class.
        """
        return [attribute for attribute in super().__dir__(cls) if attribute != '__init_subclass__']

