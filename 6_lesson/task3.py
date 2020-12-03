# Задание 3

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self._income = {'profit': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_full_profit(self):
        return f'{sum(self._income.values())}'


WORKER = Position('Вася', 'Пупкин', 'Слесарь', 1000, 5000)
print(WORKER.get_full_name())
print(WORKER.position)
print(WORKER.get_full_profit())
