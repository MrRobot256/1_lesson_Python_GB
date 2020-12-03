# Задание 1

MATRIX_A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]
MATRIX_B = [[3, 4, 5, 6], [7, 8, 9, 0], [2, 3, 6, 9]]


class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        matrix = []

        for item in range(len(self.lists)):
            matrix.append([])
            for new_item in range(len(self.lists[0])):
                matrix[item].append(self.lists[item][new_item] + other.lists[item][new_item])
        return '\n'.join(map(str, matrix))


MATRIX_1 = Matrix(MATRIX_A)
MATRIX_2 = Matrix(MATRIX_B)
print(f'Matrix 1\n{MATRIX_1}\n{"-" * 20}')
print(f'Matrix 2\n{MATRIX_2}\n{"-" * 20}')
print(f'Matrix 1 + Matrix 2\n{MATRIX_1 + MATRIX_2}')