# Создание словарей
book = {}
book['Миша'] = [12345]
book['Саша'] = [67890, 54321]
print(book)

# Поиск имени в словаре
if 'Даша' in book:
    print('yes')
else:
    print('no')

# Вывод значений построчно
for x, y in book.items():
    print(x, y)

for x in book.values():
    print(x)

for x in book.keys():
    print(x)

# моржовый оператор :=
while x:=int(input('--> ')) < 0:
    print('Введи число больше нуля')