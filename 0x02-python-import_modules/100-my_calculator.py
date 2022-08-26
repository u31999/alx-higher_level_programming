#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    from calculator_1 import add, sub, mul, div

    new_argv = argv[1:]
    if len(new_argv) != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    elif len(new_argv) == 3:
        a = int(new_argv[0])
        b = int(new_argv[2])
        operater = new_argv[1]
        if operater == '+':
            print('{} {} {} = {}'.format(a, operater, b, add(a, b)))
        elif operater == '-':
            print('{} {} {} = {}'.format(a, operater, b, sub(a, b)))
        elif opreater == '*':
            print('{} {} {} = {}'.format(a, operater, b, mul(a, b)))
        elif operater == '/':
            print('{} {} {} = {}'.format(a, operater, b, div(a, b)))
        else:
            print('Unknown operator. Available operators: +, -, * and /')
