#!/usr/bin/python3
'''MyList that inherits from list'''


class MyList(list):
    '''scrolls through the list, sorts it and we print the new list.'''
    def print_sorted(self):
        new_list = []
        for x in self:
            new_list.append(x)
        new_list.sort()
        print(new_list)
