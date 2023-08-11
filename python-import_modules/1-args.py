#!/usr/bin/python3

import sys # built-in function to access the list of command-line arguments passed to the script

def print_arguments(*args): # defines a function named print_arguments that takes a variable number of arguments.
    """Prints the number of and the list of its arguments."""

    # Get the number of arguments
    num_args = len(args)
    
    if num_args == 0:
        print("0 arguments.")  # Print message for no arguments
    else:
        if num_args == 1:
            args_str = "argument:"  # Set the string that describes the label for a single argument when printing the output
        else:
            args_str = "arguments:"  # Set the string that describes the label for a multiple arguments when printing the output
        print("{} {}".format(num_args, args_str))  # Print count and label dynamically
        for i, arg in enumerate(args, start=1): # The enumerate function generates pairs of index and value for each element (arg) in the args list
            print("{}: {}".format(i, arg))  # Print each argument's position (index) and its corresponding value in the output

if __name__ == "__main__": # Code to be executed only when the script is run directly (as the main program)
    # Test the function with command-line arguments
    args = sys.argv[1:]  # Exclude the script name from arguments
    # Call print_arguments function with command-line arguments
    print_arguments(*args) # print_arguments function and pass the elements of the args list as individual arguments to the function
