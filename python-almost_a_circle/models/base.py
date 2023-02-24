#!/usr/bin/python3
'''create class'''
import json
import os.path


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
        if json_string is None or len(json_string) == 0:
            json_string = []
            return json_string
        return json.loads(json_string)

    '''returns an instance with all attributes already set'''
    @classmethod
    def create(cls, **dictionary):
        '''create a new rectangle or square object'''
        if cls.__name__ == "Square":
            new_object_dummy = cls(1)
            new_object_dummy.update(**dictionary)
        else:
            new_object_dummy = cls(1, 2)
            new_object_dummy.update(**dictionary)
        return new_object_dummy

    ''' returns a list of instances:'''
    @classmethod
    def load_from_file(cls):
        ret = []
        filename = cls.__name__ + ".json"
        if os.path.isfile(filename):
            with open(filename, 'r') as file:
                str_list = file.read()
            dict_list = cls.from_json_string(str_list)
            for obj_dict in dict_list:
                new_obj = cls.create(**obj_dict)
                ret.append(new_obj)
        return ret
