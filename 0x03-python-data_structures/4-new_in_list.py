#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_idx = my_list[:]
    if idx < 0:
        return list_idx
    if idx > len(my_list) - 1:
        return list_idx
    list_idx[idx] = element
    return list_idx
