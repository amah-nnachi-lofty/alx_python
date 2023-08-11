#!/usr/bin/python3

# Import the entire add_0 module and access the add function using dot notation
import add_0

def main():
    # Assign values to variables a and b
    a = 1
    b = 2
    # Call the add function with variables a and b as arguments
    result = add_0.add(a, b)
    # Display the result using string formatting
    print("{} + {} = {}".format(a, b, result))

#  Ensures that the main() function is only executed when the script is run directly
if __name__ == "__main__":
    main()
