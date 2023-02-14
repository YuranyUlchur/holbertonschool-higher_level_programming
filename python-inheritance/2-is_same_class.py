#!/usr/bin/python3
''' function that returns True or False'''


def is_same_class(obj, a_class):
    '''returns True or False if is exactly an instance of class'''
    if type(obj) is a_class:
        return True
    if type(obj) != a_class:
        return False
