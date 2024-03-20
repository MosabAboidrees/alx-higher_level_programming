#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    # Use map to apply a lambda function
    # that multiplies each element by 'number'
    # to each element in 'my_list'.
    # Convert the result of map back into a list.
    return list(map((lambda x: x * number), my_list))
