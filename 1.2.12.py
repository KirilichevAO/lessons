# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

# string1 = input('Введите предложение: ')
# string2 = input('Введите слово: ')
# x = string1.count(string2)
# print(x)

# другое решение
text = 'Я люблю Python люблю'
searchText = input('Введите строку для подсчета вхождения: ')

list = text.split(searchText)
print(len(list)-1)

# другое решение
str1 = input('Введите предложение: ')
str2 = input('Введите слово: ')
len_char = len(str2)
i = 0
count = 0
while i < len(str1)-1:
    if str2.lower() == str1[i:len_char+i].lower():
        count +=1
    i += 1
print(count)