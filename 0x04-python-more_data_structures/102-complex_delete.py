#!/usr/bin/python3
def complex_delete(my_dict, value):
    delete = [key for key, val in my_dict.items() if val == value]
    for remove in delete:
        del my_dict[remove]
    return my_dict
