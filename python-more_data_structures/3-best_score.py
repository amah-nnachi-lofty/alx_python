#!/usr/bin/python3

# Define a function that returns the key with the highest value in a dictionary
def best_score(a_dictionary):
    """
    Returns the key with the highest value in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to search.

    Returns:
        The key with the highest value, or None if the dictionary is empty.

    Note:
        If multiple keys have the same highest value, the first one encountered
        will be returned.
    """
    # Check if the dictionary is empty or None
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    # Find the maximum value in the dictionary
    max_score = max(a_dictionary.values())
    
    # Iterate through the dictionary to find the key with the max_score
    for key, value in a_dictionary.items():
        if value == max_score:
            return key
