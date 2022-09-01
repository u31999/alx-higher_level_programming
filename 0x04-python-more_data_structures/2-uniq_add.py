#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_set = set(my_list)
    result = 0
    for x in list_set:
        result += x
    return result
