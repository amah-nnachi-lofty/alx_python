#!/usr/bin/python3
import random
# Generate a random signed number between -10000 and 10000
number = random.randint(-10000, 10000)
# Calculate the absolute value of the number and get the last digit
abs_number = abs(number)
last_digit = abs_number % 10
# Print the formatted output based on the conditions
output_string = "Last digit of{} is{} ".format(number, last_digit)
if last_digit > 5:
    output_string += " and is greater than 5"
elif last_digit == 0:
    output_string += " and is 0"
else:
    output_string += " and is less than 6 and not 0"
# Print the final output on a single line
print(output_string)
