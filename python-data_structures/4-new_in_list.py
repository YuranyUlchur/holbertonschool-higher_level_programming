#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    len_list = len(my_list)
    new_list = my_list.copy()
    if idx < 0:
        return new_list
    if len_list == idx:
        idx = element
        return new_list
    for x in range(0, len_list):
        if x == idx:
            new_list[x] = element
            return new_list
