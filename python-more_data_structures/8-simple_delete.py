#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    del a_dictionary[key]
    return a_dictionary


def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")


a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
new_dict = simple_delete(a_dictionary, 'track')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")

