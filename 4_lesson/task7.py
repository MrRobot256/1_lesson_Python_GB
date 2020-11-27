# Задание 7

from itertools import  count
from math import factorial

def generate_factorial():
    for element in count(1):
        yield factorial(element)


GENERATE = generate_factorial()
NUMBER = 0

for item in GENERATE:
    if NUMBER == 15:
        break
    else:
        NUMBER += 1
        print(f'Факториал числа {NUMBER} = {item}')