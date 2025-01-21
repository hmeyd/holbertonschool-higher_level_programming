#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0
    R_list ={"I" : 1, "V" : 5, "X" : 10, "L": 50, "C" : 100, "D" : 500, "M" : 1000}
    for i in range(len(roman_string)):
        if i < len(roman_string) - 1:
            if roman_string[i] == "I" and (roman_string[i + 1] == "V" or roman_string[i + 1]  == "X"):
                sum = sum + R_list[roman_string[i]] - 2
                i = i + 1
            else:
                sum = sum + R_list[roman_string[i]]
        else:
            sum = sum + R_list[roman_string[i]]
    return(sum)
    

roman_number = "IV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))






