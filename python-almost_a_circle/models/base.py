#!/usr/bin/python3
'''create class'''
import json


class Base:
    '''private attribute'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''validation'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    '''returns the JSON string representation'''
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return"[]"
        return json.dumps(list_dictionaries)
