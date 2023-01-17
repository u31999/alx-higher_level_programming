#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    new_argv = argv[1:]
    result = 0

    for num in new_argv:
        result += int(num)
    print(result)
