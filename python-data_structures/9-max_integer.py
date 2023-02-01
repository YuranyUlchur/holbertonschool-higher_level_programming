#!/usr/bin/python3
def max_integer(my_list=[]):
    len_list = len(my_list)
    if my_list == None:
        return None
    max_list = reduce(my_list)
    print(max_list)