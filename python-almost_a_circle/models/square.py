#!/usr/bin/python3
"""create class Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of a square."""
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """The size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """that assigns an argument to each attribute"""
        if args:
            order = ["id", "size", "x", "y"]
            for index, arg in enumerate(args):
                setattr(self, order[index], arg)

        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """that returns the dictionary representation of a Square"""
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
