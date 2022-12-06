# Реализуйте алгоритм задания случайных чисел 
# без использования встроенного генератора псевдослучайных чисел.

# import time
# seconds = time.time()

# # seconds = time.time()
# # print(seconds)
# # seconds = round(seconds % 1 * 10)
# # print(seconds)

# Другой вариант решения через функцию
import time
seconds = time.time()

def my_random(a):
    a = round(a % 1 * 10)
    return a

print(my_random(seconds))