#!/usr/bin/python3
"""Square that defines a square"""


class Square:
    """Instantiation with size"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    """retrieve it"""
    @property
    def size(self):
        return (self.__size)

    """property setter to set it"""
    @size.setter
    def size(self, value):
        self.__size = value
        """size must be an integer"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    """Private instance attribute: position"""
    """get the value of an attribute"""
    @property
    def position(self):
        return (self.__position)

    """assign a value to an attribute"""
    @position.setter
    def position(self, value):
        self.__position = value
        """size must be an integer"""
        for p in self.__position:
            if type(p) != int:
                raise TypeError("position must\
 be a tuple of 2 positive integers")

        """Public instance method"""
    def area(self):
        return(self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print("{}".format("\n" * self.__position[1]), end="")
            for i in range(self.__size):
                print("{}".format(" " * self.__position[0]), end="")
                for x in range(self.__size):
                    print('#', end='')
                print()
