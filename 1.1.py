# Типы данных и переменная
# int, float, boolean, str, list, None

# value = None  # присвоение значения переменной
# print(type(value))  # вывод тип переменной

# a = 123  # присвоение значения переменной
# b = 1.23
# print(a)  # вывод значения переменной
# print(b)

# value = 12334  # присвоение значения переменной
# print(type(value))  # вывод тип переменной

# s = 'hello world' # присвоение значения переменной
# s = "'hello world'"  # присвоение значения переменной
# print(s)  # вывод значения переменной

# print(a, b, s)
# print(a, '-', b, '-', s)
# print('{} - {} - {}'.format(a, b, s))
# print('{2} - {1} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = True
# print(f)

# list = [1, 2, 3]  # массив
# print(list)

# Ввод и вывод данных
# print, input

# print('Введите a') # выводим запрос на ввод числа
# a = input() # присваеваем переменной введенное число
# print('Введите b') # выводим запрос на ввод числа
# b = input() # присваеваем переменной введенное число
# print(a, b) # разные форматы представления
# print('{} {}'.format(a, b)) # разные форматы представления
# print(f'{a} {b}') # разные форматы представления
# print(a, '+', b, '=', a+b) # вывод челочисленных значений строкой

# print('Введите a')
# a = int(input())
# print('Введите b')
# b = int(input())
# print(a, '+', b, '=', a+b) # вывод суммы челочисленных значений

# print('Введите a')
# a = float(input())
# print('Введите b')
# b = float(input())
# print(a, '+', b, '=', a+b)  # вывод суммы чисел с плавающей точкой

# Арифметические операции
# +, -, *, /, %, //, **
# **, ⊕, ⊖, *, /, //, %, +, -
# (), Сокращенные операции

# a = 123
# b = 321
# c = a+b
# print(c)

# a = 1.3
# b = 3
# c = a*b
# print(c)

# a = 1.3
# b = 3
# c = round(a*b) # округление
# print(c)

# a = 1.3234345
# b = 3
# c = round(a*b, 5) # число символов после запятой
# print(c)

# a = 3
# a = a + 5
# print(a)

# a = 3
# a += 5 # сокращенное отображение 
# print(a)

# Логические операции
# >, >=, <, <=, ==, !=
#not, and, or – не путать с &, |, ^
# is, is not, in, not in
# gen

# a = 1 > 3
# a = 1 < 3 and 5 > 2
# print(a)

# Управляющие конструкции
# if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша!')
# elif username == 'Марина':
#     print('Я так ждал Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ!')
# else:
#     print('Привет, ', username)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# Управляющие конструкции
# for

# for i in 1, 2, 3, 4, 5:
#     print(i**2)

# list = [1, 2, 3, 4, 5]
# for i in list:
#     print(i)

# r = range(10)
# for i in r:
#     print(i)

# for i in range(10):
#     print(i)

# for i in 'qwerty':
#     print(i)

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
arg = 1
print(f(arg))
print(type(f(arg)))