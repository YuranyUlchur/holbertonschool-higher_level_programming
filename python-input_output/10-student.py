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
        for i in attrs:
            '''returns True if the object has an attribute'''
            if hasattr(self, i):
                '''get the value of an attribute'''
                new_dict[i] = getattr(self, i)
        '''return the new dictionary'''
        return new_dict
