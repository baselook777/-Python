# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg_1,arg_2,arg_3):
    max_1 = arg_1
    if arg_2 >= arg_1:
        max_1 = arg_2
        max_2 = arg_1
    else:
        max_2 = arg_2
    if arg_3 >= arg_2:
        max_2 = arg_3
    summa_max = max_1 + max_2
    return summa_max

print(my_func(10, -2, 0))