#!/usr/bin/python3
'''Read a text file (UTF8)'''


def read_file(filename=""):
    '''Read file'''
    with open(filename, "r", encoding="utf-8") as file:
        for text in file:
            print(text, end="")
