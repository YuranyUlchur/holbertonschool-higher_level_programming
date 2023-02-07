#!/usr/bin/python3
"""Square that defines a square"""


class Square:
    """Instantiation with size"""
    def __init__(self, size=0):
        self.size = size

    """retrieve it"""
    @property
    def size(self):
        return (self.__size)

    """property setter to set it"""
    @size.setter
    def position(self, value):
        self.__position = value
        if (type(self.__position) != 2 or
                not all(isinstance(x, int) and x >= 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        """Public instance method"""
    def area(self):
        return(self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for x in range(self.__size):
                    print('#', end='')
                print()
