#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    
    sum = 0
    R_list = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }

    for i in range(len(roman_string)):
        if i < len(roman_string) - 1:
            if R_list[roman_string[i]] < R_list[roman_string[i + 1]]:
                sum -= R_list[roman_string[i]]
            else:
                sum += R_list[roman_string[i]]
        else:
            sum += R_list[roman_string[i]]

    return sum
