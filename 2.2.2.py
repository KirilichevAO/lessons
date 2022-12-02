# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму

def posl(a):
    return (1+1/a)**a

try:
    n = int(input('Введите число: '))
    sp = []
    for i in range(n):
        sp.append(posl(i+1))
    print(round(sum(sp)))
except:
    print('Введено некорректное значение!')
