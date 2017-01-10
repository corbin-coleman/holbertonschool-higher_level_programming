#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    my_idx = 0
    for ele in my_list:
        if my_idx == idx:
            my_list[my_idx] = element
            return (my_list)
        my_idx += 1
    return (my_list)
