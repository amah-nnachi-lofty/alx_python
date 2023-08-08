"""This program uses a for loop to iterate through numbers from 0 to 98 (inclusive),
and prints each number in both decimal and hexadecimal formats. 
The hex() function is used to convert the decimal number to its hexadecimal representation. The f-string is used for formatting the output."""
for i in range(99):
    print("{} = {}".format(i, (hex(i))))
