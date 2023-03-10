# Требуется определить, можно ли от шоколадки размером 
# n × m долек отломить k долек, если разрешается сделать
# один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

def chocolate(a, b, c):
    if a == 1 and c == 1 and b > a:
        return 'yes'
    elif (a * b - c) % 2 == 0:
        return 'yes'
    else:
        return 'no' 
    
print(chocolate(3, 2, 4))
print(chocolate(3, 2, 1))