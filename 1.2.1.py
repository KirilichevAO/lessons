# Книги для изучения. Рекомедую читать именно в таком порядке:
# Byte of Python, Swaroop C. H.
# Грокаем алгоритмы, Адитья Бхаргава
# Изучаем Python (1, 2 том), Марк Лутц
# IDE, которую использовал на семинаре: https://www.onlinegdb.com/online_python_compiler
# PyCharm: https://www.jetbrains.com/ru-ru/pycharm/
# Дзен Python: https://tyapk.ru/blog/post/the-zen-of-python

# MATCH CASE:
# Есть видос (других на русском языке не нашёл): https://www.youtube.com/watch?v=jIFeDDf69Uk&t=90s
# Есть классная статья (если будет сложно её читать, то к ней после видоса, хотя всё должно быть нормально): https://docs-python.ru/tutorial/tsikly-upravlenie-vetvleniem-python/konstruktsija-match-case/
# ПРО СОБЕСЕДОВАНИЯ:
# Тут есть интересные видео о Python и собеседования на Python-разработчиков: https://www.youtube.com/c/AndyPronin


# Напишите программу, которая на вход принимает два числа и проверяет, является ли одно число квадратом другого.
# 5, 25 -> yes
# 4, 16 -> yes
# 25, 5 -> yes
# 8, 9 -> no

try:  # конструкция которая не ломает программу при вводе недопустимых значений
    a = int(input('a = '))
    b = int(input('b = '))
    if (a * a == b) or (b * b == a): # или вариант if (a ** 2 == b) or (b ** 2 == a):
        print('yes')
    else:
        print('no')
except:  # конструкция которая не ломает программу при вводе недопустимых значений
    print('Введены некорректные данные!')