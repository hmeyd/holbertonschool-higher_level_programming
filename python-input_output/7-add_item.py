#!/usr/bin/python3
"""
function that returns the dictionary description with simple data structure
"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
my_list = []
my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename)
