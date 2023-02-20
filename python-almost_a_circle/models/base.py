#!/usr/bin/python3
'''create class'''


class Base:
    '''private attribute'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''validation'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
