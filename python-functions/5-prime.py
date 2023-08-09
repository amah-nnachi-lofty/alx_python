#!/usr/bin/python3

# Define a function to check if a number is prime
def is_prime(number):
    # Special case: 2 is the only even prime number
    if number == 2:
        return True
    # Handle cases for non-prime numbers (less than 2 or even)
    elif number < 2 or number % 2 == 0:
        return False
    else:
        # Check divisibility from 3 up to the square root of the number
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        # If no divisor is found, the number is prime
        return True
