def fibonacci_sequence(n):
    # Check if n is non-positive, return an empty list
    if n <= 0:
        return []

    # Initialize the sequence with the first two Fibonacci numbers
    sequence = [0, 1]

    # Generate the Fibonacci sequence up to the nth number
    for i in range(2, n): # indicates that the loop will start iterating from the index 2, since the initial sequence already contains the first two Fibonacci numbers (0 and 1).
        # Calculate the next Fibonacci number by summing the last two numbers
        # sequence[i - 1] refers to the last Fibonacci number that has been generated and appended to the sequence.
        # sequence[i - 2] refers to the second-to-last Fibonacci number that was generated and appended to the sequence.
        next_fibonacci = sequence[i - 1] + sequence[i - 2]  
        # Append the next Fibonacci number to the sequence
        sequence.append(next_fibonacci)

    # Return the generated Fibonacci sequence
    return sequence
