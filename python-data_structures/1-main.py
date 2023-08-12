#!/usr/bin/python3

print_matrix_integer = __import__('1-print_matrix_integer').print_matrix_integer
# Define a matrix with integer values
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Call the print_matrix_integer function to print the matrix
print_matrix_integer(matrix)
# Print a separator line
print("--")
# Call the print_matrix_integer function with an empty matrix
print_matrix_integer()