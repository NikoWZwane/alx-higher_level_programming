#!/usr/bin/python3
def element_at(my_list, idx):
    # Check if idx is within the valid range
    if 0 <= idx < len(my_list):
        return my_list[idx]
    else:
        # Return None or raise an exception if idx is out of bounds
        return None
