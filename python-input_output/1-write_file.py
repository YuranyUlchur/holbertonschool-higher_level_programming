#!/usr/bin/python3
'''write a text file (UTF8)'''


def write_file(filename="", text=""):
    '''write file'''
    with open(filename, "w", encoding="utf-8") as file:
        read_data = file.write(text)
        '''returns the number of characters written:'''
        return read_data
