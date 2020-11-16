# Задание 4

user_input = input('Введите хоть что-то: ')
word = user_input.split()
counter = 0

for line in word:
    counter += 1
    print(counter, line[:10])
