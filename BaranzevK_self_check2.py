"""
Баранцев Кирилл Петрович
редактируйте/пишите код в блоках между
---начало--- и ---конец---
Решение задачи может быть в несколько строчек, но чем меньше, тем лучше.
В случае верного решения запуск файла приведёт к выводу True для каждого задания
"""
s = 'Баранцев Кирилл Петрович'
i = 3

""" +++ ВЛОЖЕННЫЕ СПИСКИ +++ """

""" Задание №1
Создайте пустой список 'fio'
---------------начало блока редактирования----------------"""

fio = []

"""------------ конец блока редактирования----------------"""
print('№1 ' + str(fio == []))

""" Задание №2
Используя цикл while добавьте в 'fio' список букв вашей фамилии, список букв вашего имени и список букв вашего отчества
---------------начало блока редактирования----------------"""

i = 0
x = 0
fio.append([])
while i != len(s):
    if s[i] == ' ':
        fio.append([])
        x += 1
        i +=1
    else:
        fio[x].append(s[i])
        i += 1

"""------------ конец блока редактирования----------------"""
print('№2 ' + str(fio == [['Б', 'а', 'р', 'а', 'н', 'ц', 'е', 'в'], ['К', 'и', 'р', 'и', 'л', 'л'], ['П', 'е', 'т', 'р', 'о', 'в', 'и', 'ч']]))

""" Задание №3
Используя цикл for переверните каждый элемент в 'fio' задом наперёд
---------------начало блока редактирования----------------"""

for i, l in enumerate(fio):
    fio[i] = fio[i][::-1]

"""------------ конец блока редактирования----------------"""
print('№3 ' + str(fio == [['в', 'е', 'ц', 'н', 'а', 'р', 'а', 'Б'], ['л', 'л', 'и', 'р', 'и', 'К'], ['ч', 'и', 'в', 'о', 'р', 'т', 'е', 'П']]))

""" Задание №4
Получите из переменной fio 4-ю букву вашего имени и запишите её в в переменной 'char'
---------------начало блока редактирования----------------"""

char = fio[1][2]

"""------------ конец блока редактирования----------------"""
print('№4 ' + str(char == 'и'))

""" Задание №5
Получите из переменной fio 4-ю букву вашего имени и запишите её в в переменной 'char'
---------------начало блока редактирования----------------"""

char = fio[1][2]

"""------------ конец блока редактирования----------------"""
print('№5 ' + str(char == 'и'))

""" Задание №6
Создайте список fio_len и запишите в него длины вашей фамилии, имени и отчества, получив их из fio
---------------начало блока редактирования----------------"""

fio_len = [len(x) for x in fio[0:3]]

"""------------ конец блока редактирования----------------"""
print('№6 ' + str(fio_len == [8, 6, 8]))

""" Задание №7
Используя стандартную функцию min получите длину самого короткого слова из ваших ФИО
---------------начало блока редактирования----------------"""

min_len = min(fio_len)

"""------------ конец блока редактирования----------------"""
print('№7 ' + str(min_len == 6))

""" Задание №8
Используя цикл в цикле получите строку, в которой будет:
последняя буква вашей фамилии, затем имени, затем отчества,
затем предпоследния буква вашей фамилии, имени, отчества,
затем предпредпоследния буква вашей фамилии, имени, отчества,
и так до того момента, пока не закончатся символы в самом коротком слове из вашей ФИО
---------------начало блока редактирования----------------"""

chars = str()
i = 0
while i < min_len:
    for l in range(len(fio)):
        chars += fio[l][i]
    i+=1

"""------------ конец блока редактирования----------------"""
print('№8 ' + str(chars == 'влчелицивнроаиррКт'))


""" +++ СЛОВАРИ +++ """

""" Задание №9
Создайте словарь с ключами 'фамилия' 'имя' 'отчество' и соответствующими значениями ФИО задом наперёд
---------------начало блока редактирования----------------"""

d = dict()
d['фамилия'] = fio[0]
d['имя'] = fio[1]
d['отчество'] = fio[2]
reversed_fio_dict = d

"""------------ конец блока редактирования----------------"""
print('№9 ' + str(reversed_fio_dict == {'фамилия': ['в', 'е', 'ц', 'н', 'а', 'р', 'а', 'Б'], 'имя': ['л', 'л', 'и', 'р', 'и', 'К'], 'отчество': ['ч', 'и', 'в', 'о', 'р', 'т', 'е', 'П']}))

""" Задание №10
Получите список ключей словаря reversed_fio_dict
---------------начало блока редактирования----------------"""

reversed_fio_dict_keys = list(reversed_fio_dict.keys())

"""------------ конец блока редактирования----------------"""
print('№10 ' + str(reversed_fio_dict_keys == ['фамилия', 'имя', 'отчество']))

""" Задание №11
Получите список значений словаря reversed_fio_dict
---------------начало блока редактирования----------------"""

reversed_fio_dict_values = list(reversed_fio_dict.values())

"""------------ конец блока редактирования----------------"""
print('№11 ' + str(reversed_fio_dict_values == [['в', 'е', 'ц', 'н', 'а', 'р', 'а', 'Б'], ['л', 'л', 'и', 'р', 'и', 'К'], ['ч', 'и', 'в', 'о', 'р', 'т', 'е', 'П']]))

""" Задание №12
Получите список картежей, содержащий пары ключ и значение словаря reversed_fio_dict
---------------начало блока редактирования----------------"""

reversed_fio_dict_items = list(reversed_fio_dict.items())

"""------------ конец блока редактирования----------------"""
print('№12 ' + str(reversed_fio_dict_items == [('фамилия', ['в', 'е', 'ц', 'н', 'а', 'р', 'а', 'Б']), ('имя', ['л', 'л', 'и', 'р', 'и', 'К']), ('отчество', ['ч', 'и', 'в', 'о', 'р', 'т', 'е', 'П'])]))

""" Задание №13
Получите значение словаря reversed_fio_dict по ключу фамилия
---------------начало блока редактирования----------------"""

res = d['фамилия']

"""------------ конец блока редактирования----------------"""
print('№13 ' + str(res == ['в', 'е', 'ц', 'н', 'а', 'р', 'а', 'Б']))

""" Задание №14
Создайте пустой словарь chars
---------------начало блока редактирования----------------"""

chars = {}

"""------------ конец блока редактирования----------------"""
print('№14 ' + str(chars == {}))

""" Задание №15
Преобразуйте строку с вашей ФИО так, чтобы в ней были только маленькие буквы и отсутствовали пробелы
---------------начало блока редактирования----------------"""

s = 'Баранцев Кирилл Петрович'
s = ''.join(s.split())
s = s.lower()

"""------------ конец блока редактирования----------------"""
print('№15 ' + str(s == 'баранцевкириллпетрович'))

""" Задание №16
Пройдите в цикле по всем буквам своих ФИО 's' и сосчитайте количество повторений каждой буквы.
Получите список 'res' из пар (кортежей):
( <буква вашей ФИО>, <количество её появления в вашей ФИО> )
---------------начало блока редактирования----------------"""

res = {}

for i in s:
    res[i] = s.count(i)
res = list(res.items())

"""------------ конец блока редактирования----------------"""
print('№16 ' + str(res == [('б', 1), ('а', 2), ('р', 3), ('н', 1), ('ц', 1), ('е', 2), ('в', 2), ('к', 1), ('и', 3), ('л', 2), ('п', 1), ('т', 1), ('о', 1), ('ч', 1)]))


""" +++ ФУНКЦИИ +++ """

""" Задание №17
Напишите функцию kirillCharToIndex которая:
- получает на вход букву русского алфавита,
- возвращает её номер в алфавите (от 1 до 33).
Например вызов kirillCharToIndex('А') должен возвращать 1
---------------начало блока редактирования----------------"""

def kirillCharToIndex(letter):

    alphabet = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')

    return alphabet.index(letter)+1

"""------------ конец блока редактирования----------------"""
print('№17 ' + str(kirillCharToIndex("Ь") == 30))

""" Задание №18
При помощи функции kirillCharToIndex измените fio так, чтобы вместо букв, в нём были их номера в алфавите
---------------начало блока редактирования----------------"""

fio

"""------------ конец блока редактирования----------------"""
print('№18 ' + str(fio == [[3, 6, 24, 15, 1, 18, 1, 2], [13, 13, 10, 18, 10, 12], [25, 10, 3, 16, 18, 20, 6, 17]]))


""" +++ КОНЕЦ =) +++ """
