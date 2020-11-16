# Задание 3

user_input = int(input('Введите число от 1 до 12: '))

months = {
    'Зима': [12, 1, 2],
    'Весна': [3, 4, 5],
    'Лето': [6, 7, 8],
    'Осень': [9, 10, 11]
}

if user_input >= 13:
    print('Такого месяца не существует!')
else:
    for key, value in months.items():
        if value.count(user_input):
            print(f'Этот месяц относится к {key}')