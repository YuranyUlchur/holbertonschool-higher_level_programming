#!/usr/bin/python3

'''script that adds all arguments'''

import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


args = sys.argv[1:]
filename = "add_item.json"


def main():
    '''adds all arguments to a list, and then save them to a file:'''
    try:
        my_list = load_from_json_file(filename)
    except Exception:
        my_list = []
    my_list += args
    save_to_json_file(my_list, filename)


if __name__ == '__main__':
    main()
