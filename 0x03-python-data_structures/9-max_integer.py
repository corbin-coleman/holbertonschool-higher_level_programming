#!/usr/bin/python3
def max_integer(my_list):
    if not my_list:
        return (None)
    large = my_list[0]
    for i in my_list:
        if i > large:
            large = i
    return (large)
