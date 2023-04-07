
# 5 Меньшее из двух
# Пользователь вводит два целых числа. Выведите меньшее из них.


def positive():
    a = int(input('Введите число a'))
    b = int(input('Введите число b'))
    c = a
    if b < a:
        c = b
    return c

print(positive())