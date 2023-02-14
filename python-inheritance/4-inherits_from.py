#!/usr/bin/python3
''' function that returns True or False'''


def inherits_from(obj, a_class):
    '''the object is an instance of a class that inherited'''
    return isinstance(obj, a_class) and type(obj) != a_class
