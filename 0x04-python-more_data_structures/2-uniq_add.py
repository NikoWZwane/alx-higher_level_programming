#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set()
    if my_list:
        for items in my_list:
            uniq_list.add(items)
        return sum(uniq_list)
