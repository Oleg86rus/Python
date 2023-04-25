# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные
# оценки на максимальные. Напишите программу, которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.

def task_2():
    str = input('Введите строку: ')
    arr = [char for char in str]
    numbers = []
    if len(str) == 0:
        print("Ошибка, вы ввели пустую строку!")
        return 0
    for i in range(len(arr)):
        if i > 0:
            if arr[i] == arr[i - 1]:
                continue
        count = 1
        for j in range(i + 1, len(arr)):
            if arr[j] == arr[i]:
                count += 1
            else:
                break
        if count == 1:
            numbers.append(f"{arr[i]}")
        else:
            numbers.append(f"{arr[i]}{count}")
        i += count - 1
    delimiter = ''
    print(delimiter.join(numbers))
task_2()
