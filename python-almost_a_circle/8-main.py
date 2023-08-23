#!/usr/bin/python3
""" 8-main """
# Import the Rectangle class from the models.rectangle module
from models.rectangle import Rectangle

if __name__ == "__main__":
    # Create a Rectangle instance with specified attributes
    r1 = Rectangle(10, 10, 10, 10)
    print(r1)  # Print the initial rectangle

    # Update the height attribute using keyword argument
    r1.update(height=1)
    print(r1)  # Print the updated rectangle

    # Update the width and x attributes using keyword arguments
    r1.update(width=1, x=2)
    print(r1)  # Print the updated rectangle

    # Update multiple attributes using keyword arguments
    r1.update(y=1, width=2, x=3, id=89)
    print(r1)  # Print the updated rectangle

    # Update attributes using keyword arguments in a different order
    r1.update(x=1, height=2, y=3, width=4)
    print(r1)  # Print the updated rectangle
