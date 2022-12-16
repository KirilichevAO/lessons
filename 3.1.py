# def calc1(x):
#     return x + 10

# #print(calc1(10))


# def calc2(x):
#     return x*10

# #print(calc2(10))


# # сворачиваем вверху преведенные функции в функцию
# def math(op, x):
#     print(op(x))

# math(calc1, 10)
# math(calc2, 10)
#####################################################


# # усложняем функцию и повторяем то же самое
# def sum(x, y):
#     return x + y


# def mult(x, y):
#     return x * y


# def calc(op, a, b):
#     print(op(a, b))
# #    return op(a, b)


# calc(mult, 4, 5)
#####################################################


############
## lambda ## - функция без имени, используется там где необходимо выполнить небольшие задачи и при этом не создавать отдельную функцию
############

# # переписываем верхние функции по новому синтаксису
# sum = lambda x, y: x + y
# mult = lambda x, y: x * y
# calc = lambda op, a, b: op(a, b)
# print(calc(mult, 4, 5))
#####################################################


# # делаем еще проще
# sum = lambda x, y: x + y
# #mult = lambda x, y: x * y # вставляем в нижнюю тем самым сокращаем код
# calc = lambda op, a, b: op(a, b)
# #print(calc(mult, 4, 5)) # было
# print(calc(lambda x, y: x * y, 4, 5)) # стало
#####################################################

########################
## List Comprehension ## - получение новых коллекций
########################

# list = [] # было
# for i in range(1, 21):
#     list.append(i)

# print(list)


# list = [i for i in range(1, 21)] # стало
# print(list)
#####################################################


# list = [] # было
# for i in range(1, 21):
#     if (i % 2 == 0):
#         list.append(i)

# print(list)


# list = [i for i in range(1, 21) if i % 2 == 0] # стало
# print(list)


# list = [(i, i) for i in range(1, 21) if i % 2 == 0] # с кортежами
# print(list)
#####################################################


# def f(x):
#     return x**3

# list = [f(i) for i in range(1, 21) if i % 2 == 0]
# print(list)


# def f(x):
#     return x**3

# list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0] # с кортежами
# print(list)
#####################################################


# f = open('f.txt', 'r') # было
# data = f.read() + ' '
# f.close()

# numbers = []

# while data != '':
#      space_pos = data.index(' ')
#      numbers.append(int(data[:space_pos]))
#      data = data[space_pos+1:]
# out = []
# for e in numbers:
#      if not e % 2:
#          out.append((e, e **2 ))
# print(out)


# def select(f, col): # стало
#     return [f(x) for x in col]
# def where(f, col):
#     return [x for x in col if f(x)]
# data = '1 2 3 5 8 15 23 38'.split()
# data = select(int, data)
# data = where(lambda e: not e % 2, data)
# data = list(select(lambda e: (e, e**2), data))

#########
## Map ## - функция применяемая к каждому элементу
#########


# li = [x for x in range(1, 20)]
# li = list(map(lambda x: x + 10, li))
# print(li)
#####################################################


# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res = map(int, data)
# res = where(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)
#####################################################


############
## Filter ##
############


# data = [x for x in range(10)]
# res = list(filter(lambda x: not x % 2, data))
# print(res)
#####################################################


# data = '1 2 3 5 8 15 23 38'.split()

# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)
#####################################################


#########
## Zip ## - формирует пары из элементов
#########


users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data)


###############
## Enumerata ## - нумерует обьекты индексами
###############


users = ['user1', 'user2', 'user3', 'user4', 'user5']
data = list(enumerate(users))
print(data)