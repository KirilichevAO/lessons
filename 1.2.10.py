# Напишите программу, которая на вход принимает число N и выдает последовательность из N членов
# Для N = 5: 1, -3, 9, -27, 81

import math


try:
    N = int(input('Введите число: '))
    for i in range(N):
        print(math.pow(-3, i))
except:
    print('Введено некорректное значение!')