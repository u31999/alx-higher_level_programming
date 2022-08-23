#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])

output = 'Last digit of {:d} is {:d} and is'.format(number, last_digit)

if last_digit > 5:
    last = 'greater than 5'
elif last_digit < 6 and last_digit != 0:
    last = 'less than 6 and not 0'
else:
    last = '0'

print(output, last)
