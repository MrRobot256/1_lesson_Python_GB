# Задание 3

def my_func(number1, number2, number3):
    summ1 = number1 + number2
    summ2 = number1 + number3
    summ3 = number2 + number3

    if summ1 > summ2 > summ3:
        return print(summ1)
    elif summ2 > summ1 > summ3:
        return print(summ2)
    else:
        return print(summ3)


my_func(100, 20, 30)
