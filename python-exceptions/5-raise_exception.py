#!/usr/bin/python3
def raise_exception():
    try:
        out = "Exception raised"
        raise out
    except out:
        print(out)
