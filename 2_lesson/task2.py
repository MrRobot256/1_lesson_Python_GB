# Задание 2

user_input = input('Введите любые символы ыерез запятую: ')
user_list = []

for item in user_input:
    user_list.append(item)

for element in range(1, len(user_list), 2):
    user_list[element - 1], user_list[element] = user_list[element], user_list[element - 1]

print(user_list)
