#!/usr/bin/python3
"""Square that defines a square"""


class Square:
    """Instantiation with size"""
    def __init__(self, size=0):
        self.__size = size
        """size must be an integer"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
