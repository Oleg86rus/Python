# 2. Площадь
# Пользователь вводит стороны прямоугольника, выведите его площадь
#


def square():
    a = int(input('Введите сторону a'))
    b = int(input('Введите сторону b'))
    res = a * b
    return res

print(square())