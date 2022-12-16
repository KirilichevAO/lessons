# Книга: "Типизированый Python", Алексей Голобурдин (если не найдете, пишите в телеграме)
# Генераторы и их применение: https://webdevblog.ru/vvedenie-v-generatory-python/
# Регулярные выражения (всем рекомендую к просмотру!): https://www.youtube.com/watch?v=8sv-6AN0_cg&t=864s
# Экспресс в tkinter: https://www.youtube.com/watch?v=t2w1L2MvOGY
# Справочник по tkinter: https://pythonru.com/uroki/obuchenie-python-gui-uroki-po-tkinter
# https://discord.gg/MVbWAEcmх
# @slava_BENG
##########################################################################################


# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 'Я люблю Джавуабв абви Питон'
# 'Я люблю Питон'

# # было
# my_str = 'Я люблю Джавуабв абви Питон'
# list = my_str.split()
# my_list = []
# for i in list:
#     if 'абв' not in i:
#         my_list.append(i)
# print(*my_list)


# # стало
# my_str = 'Я люблю Джавуабв абви Питон'
# list = my_str.split()
# my_list = [i for i in list if 'абв' not in i]
# print(*my_list)


# или так
my_str = 'Я люблю Джавуабв абви Питон'
filtered_list = list(filter(lambda word: "абв" not in word, my_str.split(" ")))

