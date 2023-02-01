#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    len_list = len(my_list)
    for x in range(1, len_list):
        if x == idx:
            del my_list[x]
            return my_list
