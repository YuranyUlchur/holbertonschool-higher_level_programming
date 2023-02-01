#!/usr/bin/python3
def max_integer(my_list=[]):
    len_list = len(my_list)
    max = 0
    if len_list == 0:
        return None
    for x in my_list:
        if x > max:
            max = x
    return max
