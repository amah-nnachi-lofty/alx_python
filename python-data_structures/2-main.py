#!/usr/bin/python3

multiple_returns = __import__('2-multiple_returns').multiple_returns

sentence = "At Holberton school, I learnt C!"
length, first = multiple_returns(sentence)  # Call the multiple_returns function
# Print the result using string formatting
print("Length: {:d} - First character: {}".format(length, first))