#!/usr/bin/python3
'''class Student defines a student'''


class Student:
    '''attributes the class student'''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    '''retrieves a dictionary representation of a Student'''
    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for i in attrs.keys():
            if i in attrs:
                new_dict[i] = attrs[i]
        return new_dict
