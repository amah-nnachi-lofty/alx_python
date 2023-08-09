#!/usr/bin/python3
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)

    if abs(celsius + 273.15) < 0.001: # To manage floating point precision for -459.67
        return -273.15

    return celsius