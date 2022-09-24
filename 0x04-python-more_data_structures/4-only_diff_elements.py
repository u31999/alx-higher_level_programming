#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    for x in set_1:
        if x in set_2:
            e_to_remove = x
    r = set_1.union(set_2)

    if e_to_remove:
        r.discard(e_to_remove)
    return r
