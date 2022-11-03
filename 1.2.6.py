sp = []
sp.append(True)
sp = sp + [1213, "abba", 54654, [1,2,3,5]]
print(sp)

sp.insert(0, 999)
print("after insert", sp)

print(sp[-1])

print(sp[-1][-1])

a = sp.pop(-1) # вырезание значения на -1 индексе
print("after pop", a)

a.remove(2) # удаление из списка занчение 2
print("after remove", a)

for i in a:
    print(i)

mas2dim = []
for i in range(5):
    temp = []
    for j in range(5):
        temp.append(i+j)
    mas2dim.append(temp)
print(mas2dim)

for i in range(len(mas2dim)):
    print(mas2dim[i])

