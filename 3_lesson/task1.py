# Задание 1

USER_INPUT1 = int(input('Введите 1 число: '))
USER_INPUT2 = int(input('Введите 1 число: '))


def get_result_by_division(number1, number2):
    if number2 == 0:
        return print('На ноль делить нельзя!')
    else:
        result_number = number1 / number2
    return print(result_number)


get_result_by_division(USER_INPUT1, USER_INPUT2)
