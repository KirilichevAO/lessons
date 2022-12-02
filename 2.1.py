# Создание текстового файла и редактирование его
# a – открытие для добавления данных
# r – открытие для чтения данных
# w – открытие для записи данных
# w+, r+

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors)
# data.close()

# Другой вариант представления кода

# with open('file.txt', 'a') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# Чтение данных из файла

# path = 'file.txt'
# data = open (path, 'r')
# for line in data:
#     print(line)
# data.close

# Используем ранее написанную функцию из файла с первой лекции перенеся ее в отдельный файл

# import function
# print(function.f(1))

# import function as f # Для ленивых))
# print(f.f(1))

# Функция с множеством параметров

# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res
# #print(concatenatio('a', 's', 'd', 'w'))
# #print(concatenatio('a', '1'))
# print(concatenatio(1, 2, 3, 4))

# Кортеж

# a = (3, 4)
# print(a)
# print(a[0])
# print(a[-1])

a = (3, 4, 5, 6)
for item in a:
    print(item)
