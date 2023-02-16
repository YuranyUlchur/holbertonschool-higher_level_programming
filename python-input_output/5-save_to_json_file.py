#!/usr/bin/python3
'''import json'''
import json
''' function JSON'''


def save_to_json_file(my_obj, filename):
    '''function that writes an Object to a text file using a JSON'''
    with open(filename, "w", encoding="utf-8") as file:
        json_object = (json.dumps(my_obj))
        read_data = file.write(json_object)
        return read_data
        