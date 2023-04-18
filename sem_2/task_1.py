# Дан список чисел. Определите, сколько в нем встречается различных чисел.

def task_1():
    list = []
    count = 0
    while True:
        num = input('Введите число: ')
        list.append(num)
        if list[len(list) - 1].isnumeric() == True:
            list[len(list) - 1] = int(list[len(list) - 1])
            count += 1
        else:
            list.remove(num)
            break
    myset = set(list)
    print(myset)
    print(len(myset))

task_1()
