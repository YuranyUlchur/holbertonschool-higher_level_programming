#!/usr/bin/python3
'''import the base class from the module'''
from models.base import Base


class Rectangle(Base):
    '''Class constructor'''
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' this super call with use the logic of the init of the Base class'''
        super().__init__(id)
        '''Assign each argument '''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
