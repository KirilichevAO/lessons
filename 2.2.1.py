def summa1():
    a = 3
    b = 6
    print(a+b)


def summa2():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    return a+b


x1 = 6
x2 = 5

def summa3():
    return x1+x2


sum = 0

def summa4():
    global sum
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    sum = a+b


def summa5(a, b):
    return a+b

try:
    a1 = int(input('Введите первое число: '))
    b1 = int(input('Введите второе число: '))
    print(summa5(a1, b1))
except:
    print('Введены некорректные данные!')
