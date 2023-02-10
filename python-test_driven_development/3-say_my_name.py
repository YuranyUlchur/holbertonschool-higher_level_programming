#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    if first_name and last_name:
        print("My name is {} {}".format(first_name, last_name))
    elif first_name:
        print("My name is {}".format(first_name))
    elif last_name:
        print("My name is {}".format(last_name))
