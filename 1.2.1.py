# Напишите программу, которая на вход принимает два числа и проверяет, является ли одно число квадратом другого.
# 5, 25 -> yes
# 4, 16 -> yes
# 25, 5 -> yes
# 8, 9 -> no

a = int(input('a = '))
b = int(input('b = '))

if (a * a == b) or (b * b == a):
    print('yes')
else:
    print('no')