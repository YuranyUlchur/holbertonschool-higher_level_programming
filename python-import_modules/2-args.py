#!/usr/bin/python3
import sys
if __name__ == '__main__':
    args = sys.argv
    i = len(args)
    if i == 1:
        print("0 arguments.")
    elif i == 2:
        print("1 argument:")
        print("1:", sys.argv[1])
    else:
        print(f"{i -1} arguments:")
        for x in range(1, i):
            print("{}: {}".format(x, sys.argv[x]))
