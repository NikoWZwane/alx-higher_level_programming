#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for int_list in my_list[::-1]:
            print("{:d}".format(int_list))
