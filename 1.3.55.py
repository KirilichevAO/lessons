# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from math import sqrt


x1 = float(input('Введите значение x1: '))
y1 = float(input('Введите значение y1: '))
x2 = float(input('Введите значение x2: '))
y2 = float(input('Введите значение y2: '))

result = sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(round(result, 2))
