# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 5 6 7 9


with open('f.txt', 'r') as data:
    my_str = data.readline()
print(my_str)

my_lst = my_str.split()
lst2 = []
for i in range(0, len(my_lst) - 1):
    my_lst[i] = int(my_lst[i])
    if int(my_lst[i]) + 1 != int(my_lst[i + 1]):
        lst2.append(my_lst[i] + 1)
print(lst2)

