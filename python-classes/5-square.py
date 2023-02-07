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
    def size(self, size):
        self.__size = size
        """size must be an integer"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        """Public instance method"""
    def area(self):
        return(self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                for i in range(self.__size):
                    print('#', end='')
                print()
