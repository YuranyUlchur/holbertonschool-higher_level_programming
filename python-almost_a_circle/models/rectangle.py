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

    ''' access the attribute value.'''
    @property
    def width(self):
        return self.__width

    '''update the value of the attribute'''
    @width.setter
    def width(self, value):
        self.__width = value
        return self.__width

    ''' access the attribute value.'''
    @property
    def height(self):
        return self.__height

    '''update the value of the attribute'''
    @height.setter
    def height(self, value):
        self.__height = value
        return self.__height

    ''' access the attribute value.'''
    @property
    def x(self):
        return self.__x

    '''update the value of the attribute'''
    @x.setter
    def x(self, value):
        self.__x = value
        return self.__x

    ''' access the attribute value.'''
    @property
    def y(self):
        return self.__y

    '''update the value of the attribute'''
    @y.setter
    def y(self, value):
        self.__y = value
        return self.__y
