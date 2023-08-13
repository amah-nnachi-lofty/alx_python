#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
  return list(map(lambda x: x * number, my_list))# Use map to apply the lambda function to each element of the list. The lambda function multiplies each element by the given number   