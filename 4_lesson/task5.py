# Задание 5

from functools import reduce


def get_list(element_1, element_2):
    return element_1 * element_2


new_list = [element for element in range(100, 1001, 2)]
print(f'Список отсортированных элементов: {new_list}\n'
      f'Список произведения всех элементов в списке: {reduce(get_list, new_list)}')
