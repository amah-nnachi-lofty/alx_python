#!/usr/bin/python3

# Define the multiple_returns function that returns a tuple with the length of a string and its first character
def multiple_returns(sentence):
    # Check if the sentence is not empty
    if sentence:
        length = len(sentence)  # Calculate the length of the sentence
        first_character = sentence[0]  # Get the first character of the sentence
    else:
        length = 0  # Set length to 0 for empty sentence
        first_character = None  # Set first_character to None for empty sentence
    return length, first_character  # Return a tuple with length and first character