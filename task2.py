# Задание 2

user_input = int(input('Введите число в секундах: '))
system_seconds = user_input
system_mins = system_seconds // 60
system_hours = system_mins // 60

if user_input > 60:
    system_seconds = user_input % 60

if system_mins > 60:
    system_mins = system_mins % 60

print(f'{system_hours}:{system_mins}:{system_seconds}')