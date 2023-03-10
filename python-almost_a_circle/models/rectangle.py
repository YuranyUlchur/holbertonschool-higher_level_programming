#!/usr/bin/python3
'''import the base class from the module'''
from models.base import Base


class Rectangle(Base):
    '''Class constructor'''
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' this super call with use the logic of the init of the Base class'''
        super().__init__(id)
        '''Assign each argument '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    ''' access the attribute value.'''
    @property
    def width(self):
        return self.__width

    '''update the value of the attribute'''
    @width.setter
    def width(self, value):
        self.__width = value
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

    ''' access the attribute value.'''
    @property
    def height(self):
        return self.__height

    '''update the value of the attribute'''
    @height.setter
    def height(self, value):
        self.__height = value
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")

    ''' access the attribute value.'''
    @property
    def x(self):
        return self.__x

    '''update the value of the attribute'''
    @x.setter
    def x(self, value):
        self.__x = value
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")

    ''' access the attribute value.'''
    @property
    def y(self):
        return self.__y

    '''update the value of the attribute'''
    @y.setter
    def y(self, value):
        self.__y = value
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")

    '''returns the area value of the Rectangle instance.'''
    def area(self):
        '''value'''
        return self.width * self.height

    '''prints in stdout the Rectangle'''
    def display(self):
        '''scroll through and print the character'''
        for x in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    '''represents an object'''
    def __str__(self):
        '''return'''
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.__x, self.__y,
                        self.__width, self.__height))

    '''assigns an argument to each attribute'''
    def update(self, *args, **kwargs):
        ''' assigns'''
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            elif i == 1:
                self.__width = args[i]
            elif i == 2:
                self.__height = args[i]
            elif i == 3:
                self.__x = args[i]
            elif i == 4:
                self.__y = args[i]
        '''assigns a key/value argument to attributes'''
        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            elif key == "width":
                self.__width = value
            elif key == "height":
                self.__height = value
            elif key == "x":
                self.__x = value
            elif key == "y":
                self.__y = value

    '''returns the dictionary representation of a Rectangle'''
    def to_dictionary(self):
        '''eturns the dictionary'''
        return {"id": self.id, "width": self.__width,
                "height": self.__height, "x": self.__x,
                "y": self.__y}
