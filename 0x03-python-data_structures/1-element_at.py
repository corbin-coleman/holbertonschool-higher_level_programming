#!/usr/bin/python3
def element_at(my_list, idx):
    my_idx = 0
    for ele in my_list:
        my_idx += 1
        if my_idx == idx + 1:
            return (ele)
    return (None)
