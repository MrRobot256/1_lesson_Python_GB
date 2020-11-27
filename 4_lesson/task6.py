# Задание 6

from itertools import count, cycle

print('Генерируем случаейные числа!')
print('Для выхода из программы нажмите "q"')

for item in count(int(input('Введите стартовое число: '))):
    print(item, end='')
    exit = input()
    if exit == 'q':
        break

print('Повторяем элементы списка и генерируем следующее число нажатием Enter')
print('Для выхода из программы нажмите "q"')

new_list = input('Введите список разделяя пробелами: ').split()
iter_new_list = cycle(new_list)
exit = None

while exit != 'q':
    print(next(iter_new_list), end='')
    exit = input()