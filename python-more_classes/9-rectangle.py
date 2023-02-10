#!/usr/bin/python3
'''class Rectangle that defines a rectangle'''


class Rectangle:
    '''class Rectangle that defines a rectangle'''
    number_of_instances = 0
    '''string representation'''
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        self.__width = value
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

    '''that returns the rectangle perimeter the rectangle'''
    def perimeter(self):
        self.__perimeter = 2 * (self.__width + self.__height)
        if self.__width == 0 or self.__height == 0:
            return (0)
        return(self.__perimeter)

    '''representation of the object'''
    def __str__(self):
        aux = ""
        if self.__width == 0 or self.__height == 0:
            return (aux)
        for i in range(self.__height):
            for x in range(self.__width):
                aux += str(self.print_symbol)
            if i != self.__height - 1:
                aux += "\n"
        return aux

    '''the rectangle to be able to recreate a new instance'''
    def __repr__(self):
        return f'Rectangle({self.__width}, {repr(self.__height)})'

    """when an instance of Rectangle is deleted"""
    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    '''the biggest rectangle based on the area'''
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1

    '''functions that create an new rectangle'''
    @classmethod
    def square(cls, size=0):
        new_rectangle = Rectangle(size, size)
        return new_rectangle
