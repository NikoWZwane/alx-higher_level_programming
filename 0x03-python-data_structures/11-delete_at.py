#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    distance = len(my_list)
    if idx > distance - 1:
        return my_list
    elif idx < 0:
        return my_list
    del my_list[idx]
    return my_list
