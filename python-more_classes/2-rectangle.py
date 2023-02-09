#!/usr/bin/python
'''class Rectangle that defines a rectangle'''


class Rectangle:
    '''class Rectangle that defines a rectangle'''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        self.__width = value
        """width must be an integer"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        self.__height = value
        """heigth must be an integer"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        return(self.__width * self.__height)

    def perimeter(self):
        self.__perimeter = 2 * (self.__width + self.__height)
        if self.__width == 0 or self.__height == 0:
            return (0)
        return(self.__perimeter)
