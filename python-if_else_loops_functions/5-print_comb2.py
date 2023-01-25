#!/usr/bin/python3
for number in range(0, 100):
    if number < 10:
        print(f"0{number}, ".format(number), end="")
    elif number > 98:
        print(f"{number}".format(number), end="")
    else:
        print(f"{number }, ".format(number), end="")
