#!/usr/bin/python3
'''function that returns True or False'''


def is_kind_of_class(obj, a_class):
    '''the object is an instance of a class that inherited'''
    if isinstance(obj, a_class):
        return True
    else:
        return False
