# Задание 4

class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'Машина: {self.name} (цвет {self.color}) полицейская машина - {self.is_police}')


    def go(self):
        print(f'{self.name}: Движение')

    def stop(self):
        print(f'{self.name}: Остановилась')

    def turn(self, direction):
        print(f'{self.name}: Машина повернула {"навело" if direction == 0 else "Направо"}')

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля составляет: {self.speed}'


class TownCar(Car):
    def show_speed(self):
        return f'{self.name}: Скорость автомобиля - {self.speed}. Превышение скорости!' \
            if self.speed > 60 else f'{self.name}: скорость автомобиля {self.speed}'


class WorkCar(Car):
    def show_speed(self):
        return f'{self.name}: Скорость автомобиля - {self.speed}. Превышение скорости!' \
            if self.speed > 40 else f'{self.name}: скорость автомобиля {self.speed}'


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


POLICE_CAR = PoliceCar('Бобик', 'белый', 80)
POLICE_CAR.go()
print(POLICE_CAR.show_speed())
POLICE_CAR.turn(0)
POLICE_CAR.stop()
print()

WORK_CAR = WorkCar('Газелька', 'серый', 90)
WORK_CAR.go()
WORK_CAR.turn(1)
print(WORK_CAR.show_speed())
WORK_CAR.turn(0)
WORK_CAR.stop()
print()

SPORT_CAR = SportCar('Ферари', 'Красная', 420)
SPORT_CAR.go()
SPORT_CAR.turn(0)
print(SPORT_CAR.show_speed())
SPORT_CAR.stop()
print()

TOWN_CAR = TownCar('КИА', 'Черный', 50)
TOWN_CAR.go()
TOWN_CAR.turn(1)
TOWN_CAR.turn(0)
print(TOWN_CAR.show_speed())
TOWN_CAR.stop()
