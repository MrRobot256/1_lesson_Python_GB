# Задание 5

class Stationery:
    def __init__(self, title='что-то рисовать'):
        self.title = title

    def draw(self):
        print(f'Начинаем {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Начинаем рисовать {self.title} ручкой')


class Pencil(Stationery):
    def draw(self):
        print(f'Начинаем рисовать {self.title} карандашм')


class Marker(Stationery):
    def draw(self):
        print(f'Начинаем рисовать {self.title} маркером')


STATIONERY = Stationery()
STATIONERY.draw()
PEN = Pen('Паркер')
PEN.draw()
PENCIL = Pencil('Инженерный')
PENCIL.draw()
MARKER = Marker('Толстый')
MARKER.draw()
