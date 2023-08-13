#!/usr/bin/python3

# Define a function that multiplies each element of a list by a given number using map
def multiply_list_map(my_list=[], number=0):
    """
    Multiplies each element of a list by a given number using map.

    Args:
        my_list (list): The list of elements to be multiplied.
        number: The number to multiply each element by.

    Returns:
        A new list with each element multiplied by the given number.
    """
    # Use map to apply the lambda function to each element of the list
    # The lambda function multiplies each element by the given number
    return list(map(lambda x: x * number, my_list))
