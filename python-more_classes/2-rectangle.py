#!/usr/bin/python
'''class Rectangle that defines a rectangle'''


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        
    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        self.__width = value
        """size must be an integer"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
    
    @property
    def height(self):
        return (self.__height)
    
    @width.setter
    def height(self, value):
        self.__height = value
        """size must be an integer"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
    
    def area(self):
        return(self.__size ** 2)
    
    def perimeter(self):
        