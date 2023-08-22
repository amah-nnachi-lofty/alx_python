#!/usr/bin/python3

"""
This module defines the Base class.

The Base class has a private class attribute `__nb_objects` and a public instance attribute `id`.

"""

class Base:
  """
  This class represents a base class.

  Args:
    id (int, optional): The id of the object. Defaults to None.
  """

  __nb_objects = 0

  def __init__(self, id=None):
    """
    Constructor of the Base class.

    Args:
      id (int, optional): The id of the object. Defaults to None.
    """

    """ Check if the id parameter is not None """
    if id is not None:
      """ Assign the value of the id parameter to the id attribute """
      self.id = id
    else:
      """ Increment the value of the __nb_objects attribute by 1 """
      self.id = Base.__nb_objects
      """ Assign the new value of the __nb_objects attribute to the id attribute """
      Base.__nb_objects += 1

