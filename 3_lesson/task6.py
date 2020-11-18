# Задание 6


def int_func():
    for word in input('Введите слова через пробел латинскими буквами: ').split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <= 122:
                chars += 1
        print(word.title() if chars == len(word) else f'{word} - не латинские буквы!')


int_func()
