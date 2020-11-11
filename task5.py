# Задание 5

proceeds = int(input('Введите вашу выручку: '))
costs = int(input('Введите ваши издержки: '))
staff_count = int(input('Введите кол-во персонала: '))
staff_salary = int(input('Введите среднюю заработную плату сотрудника: '))
profitability = proceeds - costs
profitability_percent = round((profitability / proceeds) * 100)
staff_salary_profit = profitability / staff_count

if proceeds > costs:
    print('У вас есть прибыль!')
    print(f'Рентабельность выручки в процентах составляет {profitability_percent}%')
    print(f'Ваша прибыль составляет {profitability} рублей')
    if staff_salary_profit > staff_salary:
        print('задумайтесь об увеличении ЗП сотрудникам')
        print(f'каждый сотрудник может получать {staff_salary_profit}')
    elif staff_salary_profit < staff_salary:
        print('Стоит лучше поработать или сократить персонал')
        print(f'Дополнительные расходы на ЗП персонала составляет {round(staff_salary_profit)} рублей на каждого')
    else:
        print('Осторожно, вы ушли в 0!')
elif proceeds < costs:
    print('У вас убытки!')
    print(f'Рентабельность выручки в процентах составляет {profitability_percent}%')
    print(f'Ваша прибыль составляет {profitability} рублей')
else:
    print('Внимание, у вас прибыль и убытки одинаковы!')

