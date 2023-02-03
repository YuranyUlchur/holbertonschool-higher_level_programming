#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    if a_dictionary:
        for x in sorted(a_dictionary):
            new_dictionary[x] = a_dictionary[x] * 2
    return new_dictionary
