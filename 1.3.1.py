# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# 6 -> да
# 7 -> да
# 1 -> нет

try:
    day = int(input('Введите номер дня недели: '))
    if day >= 1 and day <= 5:
        print('нет')
    elif day >= 6 and day <= 7:
        print('да')
    else:
        print('нет такого дня')
except:
    print('Введено некорректное значение!')