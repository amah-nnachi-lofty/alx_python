#!/usr/bin/python3

# Import the add function from add_0.py
from add_0 import add as my_add_function

def main():
    # Assign values to variables a and b
    a = 1
    b = 2
    # Call the add function with variables a and b as arguments
    result = my_add_function(a, b)
    # Display the result using string formatting
    print("{} + {} = {}".format(a, b, result))

#  Ensures that the main() function is only executed when the script is run directly
if __name__ == "__main__":
    main()

