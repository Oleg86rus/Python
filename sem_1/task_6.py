
# 6.Четырехзначное?
# Пользователь вводит целое число. Выведите YES, если это число является четырехзначным, и NO в противном случае.

def positive():
    a = int(input('Введите число a'))
    b = 'YES'
    if a - 1000 < 0:
        b = 'NO'
    return b

print(positive())