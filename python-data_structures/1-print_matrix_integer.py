#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers."""
    
    # Iterate through each row in the matrix
    for row in matrix:
        # Iterate through each element in the current row
        for index, value in enumerate(row):
            # Print the current element formatted as an integer
            print("{:d}".format(value), end="")
            # Check if the current element is not the last in the row
            if index < len(row) - 1:
                # Print a space to separate elements within the row
                print(" ", end="")
        # Print a new line to move to the next row
        print()