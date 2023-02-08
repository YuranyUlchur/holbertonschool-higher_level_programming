#!/usr/bin/python3
'''function that adds 2 integers.'''


def add_integer(a, b=98):
    '''comparison of int and float'''
    if(type(a) != int and type(a) != float):
        raise TypeError("a must be an integer")
    if(type(b) != int and type(b) != float):
        raise TypeError("b must be an integer")
    '''Returns an integer'''
    return(int(a + b))
