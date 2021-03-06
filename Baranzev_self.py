"""
Баранцев Кирилл Петрович
редактируйте/пишите код в блоках между
---начало--- и ---конец---
Решение задачи может быть в несколько строчек, но чем меньше, тем лучше.
В случае верного решения запуск файла приведёт к выводу True для каждого задания
"""
a = 'Баранцев Кирилл Петрович'
""" Задание №1
Запишите в переменную 'fio' список, полученный из переменной 'а' и содержащий Фамилию, Имя, Отчество
---------------начало блока редактирования----------------"""

a = a.split()
fio = list(a)

"""------------ конец блока редактирования----------------"""
print('№1 ' + str(fio == ['Баранцев', 'Кирилл', 'Петрович']))

""" Задание №2
Получите только имя из переменной 'fio' и запишите в переменную 'name'
---------------начало блока редактирования----------------"""

name = fio[1]

"""------------ конец блока редактирования----------------"""
print('№2 ' + str(name == 'Кирилл'))

""" Задание №3
Получите в переменной 'l' длину своей фамилии
---------------начало блока редактирования----------------"""

l = len(fio[0])

"""------------ конец блока редактирования----------------"""
print('№3 ' + str(l == 8))

""" Задание №4
Получите в переменной 'res' строку из третей буквы вашей Фамилии
---------------начало блока редактирования----------------"""
b = list ('Баранцев')
res = b[2]

"""------------ конец блока редактирования----------------"""
print('№4 ' + str(res == 'р'))

""" Задание №5
Получите в переменной 'res' строку из двух первых букв вашей Фамилии
---------------начало блока редактирования----------------"""

res = b[0] + b[1]

"""------------ конец блока редактирования----------------"""
print('№5 ' + str(res == 'Ба'))

""" Задание №6
Получите в переменной 'res' строку из двух последних букв вашей Фамилии
---------------начало блока редактирования----------------"""

res = b[6] + b[7]

"""------------ конец блока редактирования----------------"""
print('№6 ' + str(res == 'ев'))

""" Задание №7
Получите в переменной 'surname_list' список из букв вашей Фамилии по очереди
---------------начало блока редактирования----------------"""

surname_list = list('Баранцев')

"""------------ конец блока редактирования----------------"""
print('№7 ' + str(surname_list == ['Б', 'а', 'р', 'а', 'н', 'ц', 'е', 'в']))

""" Задание №8
Получите в переменной 'surname_tuple' кортеж из букв вашей Фамилии по очереди
---------------начало блока редактирования----------------"""

surname_tuple = tuple('Баранцев')

"""------------ конец блока редактирования----------------"""
print('№8 ' + str(surname_tuple == ('Б', 'а', 'р', 'а', 'н', 'ц', 'е', 'в')))

""" Задание №9
Получите в переменной 'res' список чётных чисел от 1 до длины вышей фамилии
---------------начало блока редактирования----------------"""

res = list(range(len('Баранцев')))
res = res [2::2]
print(res)

"""------------ конец блока редактирования----------------"""
print('№9 ' + str(res == [2, 4, 6]))

""" Задание №10
Получите в переменной 'res' список кортежей где первый элемент кортежа это номер буквы в вашей фамилии (от 0), а второй это буква вашей фамилии
---------------начало блока редактирования----------------"""

res = list()
for i in enumerate(list('Баранцев')):
	res.append(tuple(i))
print(res)

"""------------ конец блока редактирования----------------"""
print('№10 ' + str(res == [(0, 'Б'), (1, 'а'), (2, 'р'), (3, 'а'), (4, 'н'), (5, 'ц'), (6, 'е'), (7, 'в')]))

""" Задание №11
Получите в переменной 'res' из переменной surname_list список букв вашей фамилии наоборот
---------------начало блока редактирования----------------"""

surname_list = list('Баранцев')
res = list(reversed(surname_list))

"""------------ конец блока редактирования----------------"""
print('№11 ' + str(res == ['в', 'е', 'ц', 'н', 'а', 'р', 'а', 'Б']))

""" Задание №12
Получите в переменной 'res' из переменной fio строку с вашей фамилией задом наперёд
---------------начало блока редактирования----------------"""

fio = list(a)
res = ''.join(reversed(fio[0]))

"""------------ конец блока редактирования----------------"""
print('№12 ' + str(res == 'вецнараБ'))

""" Задание №13
Получите в переменной 'res' из переменной surname_list список букв вашей фамилии без третей буквы
---------------начало блока редактирования----------------"""

surname_list = list('Баранцев')
surname_list.remove(surname_list[2])
res = surname_list

"""------------ конец блока редактирования----------------"""
print('№13 ' + str(res == ['Б', 'а', 'а', 'н', 'ц', 'е', 'в']))
