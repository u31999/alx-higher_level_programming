#!/usr/bin/python3
for alpha in range(122, 96, -1):
    if alpha % 2 != 0 :
        print('{:c}'.format(alpha - 32), end='')
    else:
        print('{:c}'.format(alpha), end='')
