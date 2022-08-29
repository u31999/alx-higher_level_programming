#!/usr/bin/python3
def no_c(my_string):
    i = 0
    result = list(my_string)
    while i <= len(my_string) - 1:
        if my_string[i] == 'c' or my_string[i] == 'C':
            result[i] = ' '
        i += 1
    return "".join(result)
