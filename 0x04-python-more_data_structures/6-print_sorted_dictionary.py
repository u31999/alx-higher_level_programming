#!usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_dict = list(a_dictionary)
    for x in sorted(list_dict):
        print('{}: {}'.format(x, a_dictionary[x]))
