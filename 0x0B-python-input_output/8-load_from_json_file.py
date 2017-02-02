#!/usr/bin/python3
def load_from_json_file(filename):
    import json
    with open(filename, 'r') as my_file:
        return json.load(my_file)
