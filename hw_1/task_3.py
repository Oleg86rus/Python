# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет 
# счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no


def lucky(num):
    num_in_str = str(num)
    first_count = 0
    second_count = 0
    length = int(len(num_in_str))   
    half_length = length // 2 
    for i in range(half_length):
        first_count += int(num_in_str[i])
        second_count += int(num_in_str[length - 1 - i])
    if first_count == second_count:
        return 'yes'
    else:
        return 'no'
    
print(lucky(385916))
print(lucky(123456))