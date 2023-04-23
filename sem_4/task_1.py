# Напишите программу, которая принимает на вход строку,
# и выводит кол-во повторов каждого из символов 1 раз.
def task_1():
    arr = input('Введите строку: ').split(' ')
    for i in range(len(arr)):
        count = 0
        for j in range(i + 1, len(arr)):
            if arr[j] == arr[i]:
                count += 1
                arr[j] = f"{arr[i]}_{count}"
    delimiter = ' '
    print(delimiter.join(arr))
task_1()
