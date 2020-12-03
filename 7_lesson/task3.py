# Задание 3

class Cell:
    def __init__(self, nums):
        self.nums = nums

    def create_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return self.nums

    def __add__(self, other):
        return f'Сумма клеток: {self.nums + other.nums}'

    def __sub__(self, others):
        return self.nums - others.nums if self.nums - others.nums > 0 \
            else 'Клеток меньше чем во второй'

    def __mul__(self, other):
        return f'Умножение клеток: {self.nums * other.nums}'

    def __floordiv__(self, other):
        return f'Деление без остатка: {self.nums // other.nums}'

