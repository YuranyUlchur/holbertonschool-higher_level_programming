#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_element = my_list[:]
    for x in range(len(my_list)):
        if search == new_element[x]:
            new_element[x] = replace
    return new_element
