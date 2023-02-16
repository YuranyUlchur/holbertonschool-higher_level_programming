#!/usr/bin/python3
'''import argument'''
import sys

'''import functions'''
save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_file = __import__('6-load_from_json_file.py').load_from_json_file

args = sys.argv
filename = "add_item.json"
''' script that adds all arguments '''


def main():
    '''add arguments to a list and save to filename'''
    try:
        my_list = load_file(filename)
    except Exception:
        my_list = args[1:]
    my_list += args
    save_to_json_file(my_list, filename)


if __name__ == '__main__':
    main()
