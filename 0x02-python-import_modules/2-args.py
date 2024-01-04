#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    x = len(argv)
    if x == 1:
        print("0 arguments.")
    elif x == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(x))
        for i in range(x):
            if i == x:
                pass
            else:
                print("{}: {}".format((i + 1), argv[(i)]))
