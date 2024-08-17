#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for indx, item in enumerate(new_list):
        if item == search:
            new_list[indx] = replace
    return new_list
