# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)


def task_2():
    arr = []
    length = int(input('Введите длинну списка: '))
    for i in range(0, length):
        arr.append(int(input('Введите элемент списка(целое число): ')))

    min = int(input('Введите минимальное число диапазона: '))
    max = int(input('Введите максимальное число диапазона: '))
    for i in range(len(arr)):
        if arr[i] >= min and arr[i] <= max:
            print(i)
task_2()