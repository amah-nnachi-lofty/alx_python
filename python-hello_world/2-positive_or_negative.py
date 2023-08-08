#!/usr/bin/python3
import random

# Generate a random signed number between -10 and 10
number = random.randint(-10, 10)

# Check if the number is positive or negative and print the result
if number > 0:
    #"The number {} is positive." is a string that contains a placeholder {}. This is where the value of the number variable will be inserted.
    #.format(number) is used to replace the placeholder {} with the value of the number variable. The value of number is dynamically inserted into the string where the {} is located.
    print("{} is positive".format(number))
elif number < 0:   #he elif statement in Python stands for "else if." It is used in conditional statements to test multiple conditions in a sequence
    print("{} is negative".format(number))
else:
    print("is zero")