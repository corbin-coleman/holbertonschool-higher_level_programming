#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    my_idx = 0
    for ele in my_list:
        if my_idx == idx:
            new_list[my_idx] = element
        my_idx += 1
    return (new_list)
