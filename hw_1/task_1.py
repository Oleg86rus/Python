# Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

def summ():
    num = int(input('Введите число: '))
    res = 0
    number_as_string = str(num)
    for i in range(len(number_as_string)):
        res += int(number_as_string[i])
    return res
    
print(summ())