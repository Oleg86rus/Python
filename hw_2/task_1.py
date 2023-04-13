# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а
# некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же
# стороной. Выведите минимальное количество монет, которые нужно
# перевернуть
def coin():
    quantity = int(input('Введите количество монет на столе: '))
    count_tails = 0
    count_eagle = 0
    for i in range(quantity):
        print('Введите 0 или 1. 0 - решка, 1 - орел.')
        x = int(input())
        if x == 0:
            count_tails += 1
        else:
            count_eagle += 1
    print('Необходимо сделать действий: ')
    if count_eagle > count_tails:
        print(count_tails)
    else:
        print(count_eagle)

coin()
