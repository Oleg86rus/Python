# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ...,
# где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# # Требуется найти N-е число Фибоначчи

num = int(input('Введите число фибоначи: '))
arr = []

def task_1(num):
    if num in [1, 2]:
        return 1
    else:
        return task_1(num - 2) + task_1(num - 1)

for i in range(1, num + 1):
    arr.append(task_1(i))

print(arr[-1])