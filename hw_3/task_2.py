# Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

from random import randint
def task_2():
    length = int(input('Введите натуральное число (количество элементов в списке): '))
    num = int(input('Введите искомое число (0-10): '))
    arr = []
    res = 0
    newArr = []
    for i in range(0, length):
        arr.append(randint(0, 10))
        count = num - arr[i]
        newArr.append(count)

    if newArr[0] > 0:
        count = newArr[0]
    else:
        count = newArr[0] * -1

    for i in range(0, length):
        if newArr[i] < 0:
            newArr[i] *= -1

        if newArr[i] < count:
            count = newArr[i]
            res = i

    print(f'Список случайных чисел: {arr}')
    print(f'Самый близкий по величине элемент: {arr[res]}')

task_2()