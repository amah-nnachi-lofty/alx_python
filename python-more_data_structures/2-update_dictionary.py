#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to update.
        key (str): The key to replace or add.
        value: The value to associate with the key.

    Returns:
        dict: The updated dictionary.

    Note:
        If the key already exists in the dictionary, the value associated with
        the key will be replaced. If the key doesn't exist, a new key/value
        pair will be added.
    """
    a_dictionary[key] = value
    return a_dictionary  # Return the updated dictionary