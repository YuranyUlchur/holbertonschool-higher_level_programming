#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == None:
       return
    my_list.reverse()
    len_list = len(my_list)
    for x in range(len_list):
        print("{:d}".format(my_list[x]))
