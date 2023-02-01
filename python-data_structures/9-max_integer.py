#!/usr/bin/python3
def max_integer(my_list=[]):
    len_list = len(my_list)
    if my_list == None:
        return None
    for x in range(0, len_list):
        if len_list > len_list[x] :
            return(len_list[x])