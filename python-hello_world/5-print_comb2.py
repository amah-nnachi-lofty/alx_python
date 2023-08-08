for i in range(100):
    print("{:02}".format(i), end=", " if i < 99 else "\n") #The :02 specifies for the value to least two digits, and if it has less than two digits, leading zeros should be added.
    # If i is not less than 99 (i.e., it's the last value), it adds a newline character \n to start a new line.
