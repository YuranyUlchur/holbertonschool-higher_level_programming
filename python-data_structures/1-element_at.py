#!/usr/bin/python3
import sys


def element_at(my_list, idx):
    sys.stdout.write(str(idx))
    if idx < 0:
        return None
    if idx in range(my_list):
        return None
