# ПРО ФУНКЦИИ:
# Можно окрыть книгу "Byte of Python" и найти главу про функции, там очень хорошо раскрыта эта тема.
# Можно посмотреть о функциях тут: https://www.youtube.com/watch?v=DJAlfolEv9A
# О переменных количествах аргументов (*args, **kwargs): https://stepik.org/lesson/372076/step/1?unit=359630
# О тайп-хинтингах: https://proglib.io/p/annotacii-tipov-v-python-vse-chto-nuzhno-znat-za-5-minut-2022-01-30
# Всемогущие декораторы: https://www.youtube.com/watch?v=Va-ovLxHmus&t=2s
# Про генераторы: https://ru.hexlet.io/courses/python-declarative-programming/lessons/generator-functions/theory_unit

# Try/except: https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html
# О том, как правильно оформлять путь к файлу (базовый вариант): https://pythonworld.ru/moduli/modul-os-path.html
# Но лучше сразу так: https://www.digitalocean.com/community/tutorials/how-to-use-the-pathlib-module-to-manipulate-filesystem-paths-in-python-3-ru
# *По просьбе аналитиков: https://stepik.org/course/76/syllabus
# Это материал по мат. статистике. Там есть три части этого курса.
# Ссылка идёт на первую часть. Как её осилите, можно перейти ко второй.
# Третья - опционально. Так же, можно сразу начать знакомиться с Jupyter notebook.

# def func(a1, a2, *args, **kwargs):
#     return a1, a2, args, kwargs
# print(func(1, 2)) # (1, 2, (), {})

# def func(a1, a2, a3, *args, **kwargs):
#     return a1, a2, a3, args, kwargs
# print(func(1, a3=3, a2=2)) # (1, 2, 3, (), {})

def func(a1, a2, a3, *args, **kwargs):
    return a1, a2, a3, args, kwargs
print(func(1, 2, 3, 'fgpd', 'befbuf', 123, key1=456, key2='qwe')) # (1, 2, 3, ('fgpd', 'befbuf', 123), {'key1': 456, 'key2': 'qwe'})

exit()
def summa1():
    a = 3
    b = 6
    print(a+b)


def summa2():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    return a+b


x1 = 6
x2 = 5

def summa3():
    return x1+x2


sum = 0

def summa4():
    global sum
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    sum = a+b


def summa5(a, b):
    return a+b

try:
    a1 = int(input('Введите первое число: '))
    b1 = int(input('Введите второе число: '))
    print(summa5(a1, b1))
except:
    print('Введены некорректные данные!')
