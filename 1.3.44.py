# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

try:
    quarter = int(input('Введите номер четверти: '))
    if quarter == 1:
        print(f'Диапазон возможных координат в {quarter} четверти от - до +')
    elif quarter == 2:
        print(f'Диапазон возможных координат в {quarter} четверти от + до +')
    elif quarter == 3:
        print(f'Диапазон возможных координат в {quarter} четверти от - до -')
    elif quarter == 4:
        print(f'Диапазон возможных координат в {quarter} четверти от + до -')
except:
    print('Введена некорректная четверть!')
