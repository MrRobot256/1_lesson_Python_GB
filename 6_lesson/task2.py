# Задание 2

class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def get_full_profit(self):
        return f'{self._lenght} м * {self._width} м * 25 кг * 5 см = {(self._lenght * self._width * 25 * 5) / 1000} т'


ROAD_1 = Road(5000, 20)
print(ROAD_1.get_full_profit())
