#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    len_list = len(my_list)
    if idx < 0:
        return my_list
    if len_list == idx:
        idx = element
        return my_list
    for x in range(0, len_list):
        if x == idx:
            my_list[x] = element
            return my_list
        
