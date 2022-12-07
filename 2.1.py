# Создание текстового файла и редактирование его

# a – открытие для добавления данных
# r – открытие для чтения данных
# w – открытие для записи данных (пересоздает/создает, запись в файл)
# w+, r+

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors)
# data.close()

# Неправельная работа с файлами
# f = open('file1.txt', 'w')
# f.write('Hello, World!')
# f.close()

# # Так лучше но не идеал
# with open('file1.txt', 'r') as f_data:
#     print(f_data.read())

# # Еще лучше но не идеал
# file_path = 'file1.txt' # выносим в отдельную переменную путь к файлу
# with open(file_path, 'r') as f_data:
#     print(f_data.read())

# # Идеал
# from pathlib import Path # подключаем библиотеку которая адаптирует путь для разных ОС

# file_path = Path('file1.txt') # указываем путь
# with open(file_path, 'r') as f_data:
#     print(f_data.read())
###############################################################

# Другой вариант представления кода

# with open('file.txt', 'a') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')
###############################################################

# Чтение данных из файла

# path = 'file.txt'
# data = open (path, 'r')
# for line in data:
#     print(line)
# data.close
###############################################################

# Используем ранее написанную функцию из файла с первой лекции перенеся ее в отдельный файл

# import function
# print(function.f(1))

# import function as f # Для ленивых))
# print(f.f(1))
###############################################################

# Функции

# def new_string(symbol, count = 3):
#     return symbol * count

# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # !!!
# print(new_string(4)) # 12
###############################################################

# Функция с множеством параметров

# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res
#print(concatenatio('a', 's', 'd', 'w')) # asdw
#print(concatenatio('a', '1')) # a1
#print(concatenatio(1, 2, 3, 4)) # 10
###############################################################

# Рекурсия

# def fib(n):
#      if n in [1, 2]:
#          return 1
#      else:
#          return fib(n-1) + fib(n-2)

# list = []
# for e in range(1, 10):
#      list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34
###############################################################

# Кортеж

# a = (3, 4)
# print(a)
# print(a[0])
# print(a[-1])

# a = (3, 4, 5, 6)
# for item in a:
#     print(item)
###############################################################

# Словари

# dictionary = {}
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
# print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left'])  # ←
#  # типы ключей могут отличаться
# print(dictionary['up'])# ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐ #print(dictionary['type']) # KeyError: 'type' del dictionary['left'] # удаление элемента
# for item in dictionary:# for (k,v) in dictionary.items():
# print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →
###############################################################

# Множества

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'      
# colors.discard('red')  # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}

# q=a\
#     .union(b) \
#     .difference(a.intersection(b))
# # {1, 21, 3, 13}
######################
# values
# items            !!!!!!!!!!!!!!!!!?????????? изучить!!!!!!!
# keys
# get

# dict
# typle
# Марк Луц
#######################



