#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers in a matrix."""
    # Create an empty result matrix
    result_matrix = []
    # Iterate through each row in the input matrix
    for row in matrix:
        # Use list comprehension to compute the squared values for the current row
        squared_row = [value ** 2 for value in row]
        # Append the squared_row list to the result_matrix
        result_matrix.append(squared_row)
    return result_matrix  # Return the resulting matrix