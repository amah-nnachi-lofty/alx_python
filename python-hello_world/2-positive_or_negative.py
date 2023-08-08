#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number} is positive") #The f stands for "format" and it tells the Python interpreter to insert the value of the variable number into the string
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero")