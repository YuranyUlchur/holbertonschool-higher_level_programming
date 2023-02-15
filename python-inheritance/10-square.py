#!/usr/bin/python3
"""class Square that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A simple Square class."""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Calculates the area of the square instance"""
        return self.__size ** 2
