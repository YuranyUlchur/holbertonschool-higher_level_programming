#!/usr/bin/python3
'''write a text file (UTF8) and add a string at the end of a text file'''


def append_write(filename="", text=""):
    '''write and add in the file'''
    with open(filename, "a", encoding="utf-8") as file:
        read_data = file.write(text)
        '''returns the number of characters written:'''
    return read_data
