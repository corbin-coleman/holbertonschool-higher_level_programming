#!/usr/bin/python3
from sys import argv
import json
import os.path

save_json = __import__('7-save_to_json_file').save_to_json_file
load_json = __import__('8-load_from_json_file').load_from_json_file

my_file = 'add_item.json'
if os.path.isfile(my_file):
    my_list = load_json(my_file)
else:
    my_list = []
count = 0
for item in argv:
    if count != 0:
        my_list.append(item)
    count += 1
save_json(my_list, my_file)
