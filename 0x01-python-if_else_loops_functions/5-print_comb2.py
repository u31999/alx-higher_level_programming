#!/usr/bin/python3
for i in range(99):
    if i < 99:
        print('{:02d}, '.format(i), end='')
    else:
        print('{}\n'.format(i))
