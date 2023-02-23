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

    '''writes the JSON string representation'''
    @classmethod
    def save_to_file(cls, list_objs):
        '''new file and a new list'''
        if list_objs is None:
            list_objs = []
        new_list = []
        with open(f"{cls.__name__}.json", "w") as file:
            for i in list_objs:
                new_list.append(i.to_dictionary())
            new_list = cls.to_json_string(new_list)
            file.write(new_list)
    
    '''returns the list of the JSON string representation '''
    @staticmethod
    def from_json_string(json_string):
        '''validation'''
        if json_string is None:
            json_string = []
        return json.loads(json_string)

