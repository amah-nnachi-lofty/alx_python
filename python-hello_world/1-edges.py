#!/usr/bin/python3
# Define the variable 'word' with the value "Holberton"
word = "Holberton"
# Extract the first 3 letters of the word using slicing
word_first_3 = word[:3]
# Extract the last 2 letters of the word using slicing
word_last_2 = word[-2:]
# Extract the middle part of the word by excluding the first and last letters
middle_word = word[1:-1]
# Print the first 3 letters of the word
print("First 3 letters: {}".format(word_first_3))
# Print the last 2 letters of the word
print("Last 2 letters: {}".format(word_last_2))
# Print the middle word (without the first and last letters)
print("Middle word: {}".format(middle_word))
