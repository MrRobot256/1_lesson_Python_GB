# Задание 2
# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

USER_INPUT_NAME = input('Введите Ваше имя: ')
USER_INPUT_SURNAME = input('Введите Вашу Фамилию: ')
USER_INPUT_BIRTHDAY = int(input('Введите Ваш год рождения: '))
USER_INPUT_CITY = input('Введите Ваш город проживания: ')
USER_INPUT_EMAIL = input('Введите Ваш email: ')
USER_INPUT_PHONE = int(input('Введите Ваш телефон: '))


def get_user_result(name, surname, birthday, city, email, phone):
    return print(f'Вы {name} {surname}, '
                 f'рождены {birthday} года, '
                 f'проживаете в {city}, '
                 f'Ваш email - {email}, '
                 f'Ваш телефон {phone}.')


get_user_result(name=USER_INPUT_NAME,
                surname=USER_INPUT_SURNAME,
                birthday=USER_INPUT_BIRTHDAY,
                city=USER_INPUT_CITY,
                email=USER_INPUT_EMAIL,
                phone=USER_INPUT_PHONE)
