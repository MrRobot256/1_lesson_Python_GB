# Задание 2

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, params):
        self.params = params

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption


class Coat(Clothes):
    @property
    def consumption(self):
        print(f'Расход фабрики на пошив - {round(self.params / 6.5 + 0.5)}')
        return round(self.params / 6.5) + 0.5


class Suit(Clothes):
    @property
    def consumption(self):
        print(f'Расход фабрики на пошив - {(2 * self.params + 0.3) / 100}')
        return (2 * self.params + 0.3) / 100


COAT = Coat(77)
SUIT = Suit(170)
print(COAT + SUIT)

