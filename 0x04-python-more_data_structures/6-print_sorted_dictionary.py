#!/usr/bin/python3
def print_sorted_dictionary(d):
    for key in sorted(d.keys()):
        print(f"{key}: {d[key]}")
