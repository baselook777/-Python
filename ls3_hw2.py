# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания,
# email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def data_name ():
    print('Введите информацию о пользователе')
    name = input('Имя: ')
    surname = input('Фамилия: ')
    year_birth = input('Год рождения: ')
    city = input('Город проживания: ')
    e_mail = input('E-mail: ')
    mob_tel = input('Телефон: ')
    return print(f'{name} {surname}, {year_birth} г.р., г. {city}, e-mail: {e_mail}, моб.тел. {mob_tel}')

print(data_name())




