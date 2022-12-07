# Считать строку из набора чисел из файла. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел. Результат заисать в конец исходного файла (х1 х2).

from pathlib import Path

file_path = Path('test.txt')

with open(file_path, 'w') as f:
    f.write(input('Введите числа через пробел: '))

with open(file_path, 'r') as f:
    nums = f.read().split(' ')

nums_new = [int(i) for i in nums]
min_num = min(nums_new)
max_num = max(nums_new)

with open(file_path, 'a') as f:
    f.write(f' {min_num} {max_num}')

with open(file_path, 'r') as f:
    print(f.read())
