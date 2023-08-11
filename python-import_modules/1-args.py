#!/usr/bin/python3

import sys

def print_arguments(*args):
    """Prints the number of and the list of its arguments."""

    # Get the number of arguments
    num_args = len(args)
    
    # If there are no arguments, print a message and return
    if num_args == 0:
        print("0 arguments.")
    else:
        if num_args == 1:
            args_str = "1 argument:"
        else:
            args_str = "arguments"
        print("{}".format(args_str), num_args)
        for i, arg in enumerate(args, start=1):
            print("{}:".format(i), arg)

if __name__ == "__main__":
    # Test the function with command-line arguments
    args = sys.argv[1:]  # Exclude the script name from arguments
    # Call print_arguments function with command-line arguments
    # Test the function with various arguments
    print_arguments(*args)