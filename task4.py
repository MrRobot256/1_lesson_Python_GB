# Задание 4

user_input = int(input('Введите целое число: '))
tmp = 0
while True:
    round_name = user_input % 10
    user_input //= 10
    if round_name > tmp:
        print(round_name)
        break
