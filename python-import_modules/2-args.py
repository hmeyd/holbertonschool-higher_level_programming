#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    print(f"Number of argument(s): {num_args} argument{'s' if num_args != 1 else ''} :")
    for i in range(1, num_args + 1):
        print(f"{i}: {sys.argv[i]}")
