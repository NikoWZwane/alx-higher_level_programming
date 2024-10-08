#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,'C': 100, 'D': 500, 'M': 1000}
    integer_value = 0 
    for i in range(len(roman_string)):
        if i > 0 and roman_values[roman_string[i]] > roman_values[roman_string[i - 1]]:
            integer_value += roman_values[roman_string[i]] - 2 * roman_values[roman_string[i - 1]]
        else:
            integer_value += roman_values[roman_string[i]]
    return integer_value
