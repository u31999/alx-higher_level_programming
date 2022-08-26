#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    
    new_argv = argv[1:]
    argv_len = len(new_argv)
    
    output_num_arg = '{:d} arguments'.format(argv_len)
    
    if argv_len == 0:
        print(output_num_arg + '.')
    else:
        print(output_num_arg + ':')
        for index, value in enumerate(new_argv):
            print('{}: {}'.format(index + 1, value))
