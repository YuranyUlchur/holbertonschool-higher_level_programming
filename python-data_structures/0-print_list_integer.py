#!/usr/bin/python3
import sys


def print_list_integer(my_list=[]):
    for x in my_list:
        sys.stdout.write(str(x))
        print(end="\n")
