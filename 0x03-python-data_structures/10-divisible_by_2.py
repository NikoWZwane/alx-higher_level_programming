#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    distence = len(my_list)
    my_new = []
    for i in range(distence):
        if my_list[i] % 2 == 0:
            my_new.append(True)
        else:
            my_new.append(False)
    return my_new
