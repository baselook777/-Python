# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы
# в расчете на одного сотрудника.

revenue = int(input('Введите в рублях объем выручки: '))
cost = int(input('Введите в рублях размер издержек: '))
profit = revenue - cost
if profit > 0:
    print(f'Ваша компания получила прибыль {profit} рублей')
    number_pers = int(input('Введите численность сотрудников: '))
    profit_pers = profit / number_pers
    print(f'Прибыль на одного сотрудника составила: {profit_pers} рублей')
else:
    print(f'Ваша компания получила убыток {profit} рублей')
