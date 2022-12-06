# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['sdf13', 'fds66', '34']
# -> 3
# 'sdf13', '34'

# list = ['123', 'qwe', 'rty', '456', '7ft']
# n = input('Введите некое число: ')
# for i in list:
#     count = 0
#     i = str(i)
#     if n in i:
#         count = 1
#         print('Присутствует!')
#         break
# if count == 0:
#     print('Отсутствует')

# Другое решение
def in_list(list_, find_):
    result = False
    for i in list_:
        if find_ in i:
            result = True
    print(i)
    return result