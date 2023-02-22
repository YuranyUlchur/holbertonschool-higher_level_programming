#!/usr/bin/python3
'''import the base class from the module'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Class constructor'''
    def __init__(self, size, x=0, y=0, id=None):
        ''' this super call with use the logic of the init of the Base class'''
        super().__init__(size, size, x, y, id)

    ''' access the attribute value.'''
    @property
    def size(self):
        return self.width

    '''update the value of the attribute'''
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

    '''represents an object'''
    def __str__(self):
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y,
                        self.width))

    '''assigns an argument to each attribute'''
    def update(self, *args, **kwargs):
        ''' assigns'''
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            elif i == 1:
                self.width = args[i]
            elif i == 2:
                self.x = args[i]
            elif i == 3:
                self.y = args[i]
        if len(args) == 0:
            pass
        '''assigns a key/value argument to attributes'''
        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            elif key == "size":
                self.size = value
            elif key == "x":
                self.x = value
            elif key == "y":
                self.y = value
