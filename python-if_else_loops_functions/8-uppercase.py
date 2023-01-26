#!/usr/bin/python3
def uppercase(str):
    i = ""
    for uppercase in str:
        if ord(uppercase) in range(97, 123):
            x = ord(uppercase) - 32
            i += chr(x)
        else:
            x = uppercase
            i += x
    print("{}".format(i))
