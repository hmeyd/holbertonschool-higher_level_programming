#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import os
    import hidden_4
    names = dir(hidden_4)
    filtered_names = [name for name in names if not name.startswith("__")]
    filtered_names.sort()
    for name in filtered_names:
        print(name)
