#!/usr/bin/python3
def save_to_json_file(my_obj, filename):
    import json
    with open(filename, 'w') as my_file:
        json.dump(my_obj, my_file)
