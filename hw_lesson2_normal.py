# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math
list_1 = [2, -5, 8, 9, -25, 25, 4]
list_2 = []
for i in list_1:
    if i >= 0:
        x = int(math.sqrt(i))
        if x ** 2 == i:
            list_2.append(x)
print(list_2)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

date = input("введите дату в формате dd.mm.yyyy ")
days = {
    "01": "первое",
    "02": "второе",
    "03": "третье",
    "04": "четвертое",
    "05": "пятое",
    "06": "шестое",
    "07": "седьмое",
    "08": "восьмое",
    "09": "девятое",
    "10": "десятое",
    "11": "одинадцатое",
    "12": "двенадцатое",
    "13": "тринадцатое",
    "14": "четырнадцатое",
    "15": "пятнадцатое",
    "16": "шестандцатое",
    "17": "семнадцатое",
    "18": "восемнадцатое",
    "19": "девятнадцатое",
    "20": "двадцатое",
    "21": "двадцать первое",
    "22": "двадцать второе",
    "23": "двадцать третье",
    "24": "двадцать четвертое",
    "25": "двадцать пятое",
    "26": "двадцать шестое",
    "27": "двадцать седьмое",
    "28": "двадцать восьмое",
    "29": "двадцать девятое",
    "30": "тридцатое",
    "31": "тридцать первое",
}
months = {
    "01": "января",
    "02": "февраля",
    "03": "марта",
    "04": "апреля",
    "05": "мая",
    "06": "июня",
    "07": "июля",
    "08": "августа",
    "09": "сентября",
    "10": "октября",
    "11": "ноября",
    "12": "декабря",
}
date = date.split(".")
print(days[date[0]], months[date[1]], date[2], "года")

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random

# вариант через for in:
n = int(input("Введите количество элементов списка "))
list = []
for i in range(n):
    list.append(random.randint(-100, 100))
print(list)

# вариант через while:
n = int(input("Введите количество элементов списка "))
list = []
i = 0
while i < n:
    list.append(random.randint(-100, 100))
    i += 1
print(list)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

print("Задача-4:")

# а) неповторяющиеся элементы исходного списка:
lst = [1, 2, 4, 5, 6, 2, 5, 2]
lst2 = []
var_set = set(lst)
for i in var_set:
    lst2.append(i)
print("неповторяющиеся элементы исходного списка:", lst2)

# б) элементы исходного списка, которые не имеют повторений:
lst = [1, 2, 4, 5, 6, 2, 5, 2]
lst2 = []
for i in lst:
    if lst.count(i) == 1:
        lst2.append(i)
print("элементы исходного списка, которые не имеют повторений:", lst2)
