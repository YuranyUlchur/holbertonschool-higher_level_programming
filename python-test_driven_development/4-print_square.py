#!/usr/bin/python3
''' prints a square with the character #'''


def print_square(size):
    '''codition the size'''
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for x in range(size):
        print("#" * size)
