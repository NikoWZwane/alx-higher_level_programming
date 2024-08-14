#!/usr/bin/python3
def no_c(my_string):
    if my_string[:]:
        remove_string1 = my_string.translate({ord("c"): None})
        remove_string2 = remove_string1.translate({ord("C"): None})
        return remove_string2
    return my_string
