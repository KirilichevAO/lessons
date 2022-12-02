# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

try:
    list = []
    N = int(input('Введите число: '))
    
    for i in range(-N, N+1):
        list.append(i)
    with open('file.txt', 'r') as data:
        a = data.readline()
        b = data.readline()
    
    print(a, b)
    a = int(a)
    b = int(b)
    print(list)
    print(f'Произведение элементов = {list[a] * list[b]}')
except:
    print('Введено некорректное значение!')