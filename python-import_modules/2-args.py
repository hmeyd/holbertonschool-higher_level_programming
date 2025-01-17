#!/usr/bin/python3
import sys
if __name__ == "__main__":
    n_a = len(sys.argv) - 1
    print(f"Number of argument(s): {n_a} argument{'s' if n_a != 1 else ''} :")
    for i in range(1, num_args + 1):
        print(f"{i}: {sys.argv[i]}")
