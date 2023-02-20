#!/usr/bin/python3
'''create class'''


class Base:
    def __init__(self, id=None):
        '''goal of it is to manage id attribute in all your future'''
        if id is not None:
            self.id = id
        else:
            Base.nb_objects += 1
            self.id = Base.nb_objects
