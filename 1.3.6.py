# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
# Нельзя юзать find или count.

a = str(input('Введите предложение: '))
b = str(input('Введите слово: '))
results = 0
sub_len = len(b)
for i in range(len(a)):
    if a[i:i+sub_len] == b:
        results += 1
print(results)
