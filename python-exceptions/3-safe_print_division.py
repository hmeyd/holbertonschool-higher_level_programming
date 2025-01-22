#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        resultat = a / b
    except (ValueError, TypeError, ZeroDivisionError):
        resultat = None
    finally:
        print("Inside result: {}".format(resultat))
    return resultat
