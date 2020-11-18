# Задание 5


def get_summ():
    counter = 0

    while True:
        print('Для выхода из программы нажмите "q"')
        user_input = input('Введите числа через пробел: ').split()

        for number in user_input:
            if user_input == 'q':
                return print(counter)
            else:
                counter += int(number)
        print(f'Сумма равна {counter}')


print(get_summ())
