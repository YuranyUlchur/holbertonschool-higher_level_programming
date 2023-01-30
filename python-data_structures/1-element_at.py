#!/usr/bin/python3
def element_at(my_list, idx):
    len_list = len(my_list)
    if idx < 0:
        return None
    for x in range(0, len_list):
        if x == idx:
            return my_list[x]
