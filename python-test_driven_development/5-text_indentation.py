#!/usr/bin/python3
'''Text indentation functions'''


def text_indentation(text):
    '''print the character'''

    character = [".", ":", "?"]
    aux = 0

    if type(text) != str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if i == len(text) - 1:
            print(text[aux:i + 1], end="")
        elif text[i] in character:
            print(text[aux:i + 1], end="")
            print('\n')
            aux = i + 1
            while text[aux] == " ":
                aux += 1
