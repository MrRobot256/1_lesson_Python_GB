# Задание 1

from time import sleep


class TrafficLights:
    __color = 'Бесцветный'

    def running(self):
        while True:
            print('Светофор "Красный"')
            sleep(7)
            print('Светофор "Желтый"')
            sleep(2)
            print('Светофор "Зеленый"')
            sleep(15)
            print('Светофор "Желтый"')
            sleep(2)


LIGHTS = TrafficLights()
LIGHTS.running()
