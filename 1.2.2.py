# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них

# a = []
# for _ in range(5):
#     a.append(int(input('Введите число: ')))  # добавляем в список значения с клавиатуры

# max = 0

# for i in range(5):
#     if a[i] > max:
#         max = a[i]
#         print(f'max = {max}')
#############################################
a = []
for _ in range(5):
    # добавляем в список значения с клавиатуры
    a.append(int(input('Введите число: ')))

max = a[0]
min = a[0]
min_i = 0
max_i = 0
avg = 0

for i in range(5):
    if a[i] > max:
        max = a[i]
        max_i = i
    if a[i] < min:
        min = a[i]
        min_i = i
    avg += a[i]

print(f'max = {max}')
print(f'min = {min}')
print(f'max_i = {max_i}')
print(f'min_i = {min_i}')
print(f'Среднее = {avg/5}')
