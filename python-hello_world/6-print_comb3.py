#!/usr/bin/python3
for i in range(10):    #  first digit of the combinations.
    for j in range(10): # second digit of the combinations.
        if i == 8 and j == 9: #When i is 8 and j is 9, it means you have reached the last combination (89) in the loop
            print("{}{}".format(i, j))
        elif (i != j and j > i):  # checks whether the first digit i is not equal to the second digit and to avoid printing duplicate combinations 
            print("{}{}".format(i, j), end=", ")