#!/usr/bin/python3
for two_digits in range(0, 10):
    for combi in range(two_digits + 1, 10):
        if two_digits == 8 and combi == 9:
            print('89')
        else:
            print('{}{}, '.format(two_digits, combi), end='')
