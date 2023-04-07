# 4. Одно положительное
# Даны три целых числа: A, B, C. Проверить истинность высказывания: "Хотя бы одно из чисел A, B, C положительное".

def positive():
    a = int(input('Введите число a'))
    b = int(input('Введите число b'))
    c = int(input('Введите число с'))
    d = False
    if a > 0 or b > 0 or c > 0:
        d = True
    return d

print(positive())