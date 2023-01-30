#!/usr/bin/python3
def print_list_integer(my_list=[]):
    len_list = len(my_list)
    for x in range(len_list):
        print("{:d}".format(my_list[x]))
