#!/usr/bin/python3
word = "Holberton" # Define the variable 'word' with the value "Holberton"
word_first_3 = word[:3] # Extract the first 3 letters of the word using slicing
word_last_2 = word[-2:] # Extract the last 2 letters of the word using slicing
middle_word = word[1:-1] # Extract the middle part of the word by excluding the first and last letters
print("First 3 letters: {}".format(word_first_3))  # Print the first 3 letters of the word
print("Last 2 letters: {}".format(word_last_2))  # Print the last 2 letters of the word
print("Middle word: {}".format(middle_word))  # Print the middle word (without the first and last letters)
