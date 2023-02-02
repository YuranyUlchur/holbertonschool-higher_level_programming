#!/usr/bin/python3
def search_replace(my_list, search, replace):
    len_list = len(my_list)
    new_element = my_list[:]
    for x in range(len_list):
        if search == new_element[x]:
            new_element[x] == replace
    return new_element
