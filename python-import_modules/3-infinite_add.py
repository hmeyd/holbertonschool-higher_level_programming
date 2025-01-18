#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv) - 1
    total = 0
    for i in range(argc):
        total += int(argv[i+1])
    print(total)
