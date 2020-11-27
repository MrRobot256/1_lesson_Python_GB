# Задание 4

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

new_list = [element for element in my_list if my_list.count(element) == 1]
print(f'Было: {my_list}\n Стало: {new_list}')