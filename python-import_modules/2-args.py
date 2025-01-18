#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv) - 1
    if (argc == 0):
        print("0 arguments.")
    elif (argc == 1):
        print("{} argument:".format(argc, end=""))
    else:
        print("{} arguments:".format(argc))
    for i in range(argc):
        print("{}: {}".format(i + 1, argv[i+1]))
