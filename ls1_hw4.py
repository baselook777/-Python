# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while
# и арифметические операции.

a = input('Введите целое положительное число: ')
str_length = len(a)
i = 0
a_max = a[0]
while i < str_length:
    if a[i] >= a_max:
        a_max = a[i]
    i = i + 1
print(f'Самая большая цифра в числе: {a_max}')