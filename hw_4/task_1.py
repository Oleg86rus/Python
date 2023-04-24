# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


def task_1():
    firstArrLength = int(input('Введите длинну первого списка: '))
    secondArrLength = int(input('Введите длинну первого списка: '))
    firstArr = []
    secondArr = []
    res = []
    for i in range(firstArrLength):
        firstArr.append(int(input('Введите элемент первого списка (целое число): ')))

    for i in range(secondArrLength):
        secondArr.append(int(input('Введите элемент второго списка (целое число): ')))

    if firstArrLength < secondArrLength:
        count = firstArrLength
    else:
        count = secondArrLength

    for i in range(count):
        if firstArr[i] in secondArr:
            res.append(firstArr[i])
    print(f'Полученный список: {res}')
    res.sort()
    print(f'Отсортированный список: {res}')

task_1()