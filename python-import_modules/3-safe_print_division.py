# 3-safe_print_division.py

def safe_print_division(a, b):
    """Divides two integers and returns the result, handling division by zero."""
    try:
        result = a / b  # Try to perform the division
    except ZeroDivisionError:
        result = None  # Handle division by zero by setting result to None
    else:
        print("Inside result: {}".format(result))  # Print the result of successful division
    finally:
        if result is None:
            print("Inside result: None")  # Print result for division by zero
        return result  # Return the result, regardless of success or failure
