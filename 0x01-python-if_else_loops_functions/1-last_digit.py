#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])

output = 'Last digit of {:d} is {:d} and is'.format(number, last_digit)

if last_digit > 5:
    last = 'greater than {}'.format(5)
elif last_digit < 6 and last_digit != 0:
    last = 'less than {} and not {}'.format(6, 0)
else:
    last = '{}'.format(0)

print(output, last)
