#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dict = {}
    for key in my_dict:
        new_dict.update({key: my_dict[key] * 2})
    return new_dict
