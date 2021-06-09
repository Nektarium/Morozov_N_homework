# Все задачи текущего блока решите с помощью генераторов списков!

import random

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

numbers = [1, 2, 4, 0]
sq_numbers = [i ** 2 for i in numbers]
print(sq_numbers)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

list_1 = ["orange", "apple", "ginger", "pear", "banana"]
list_2 = ["cherry", "pear", "orange", "grape", "raspberry"]
mutual_list = [i for i in list_1 if i in list_2]
print(mutual_list)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

numbers = [random.randint(-10, 10) for _ in range(10)]
new_numbers = [i for i in numbers if i > 0 and i % 3 == 0 and i % 4 != 0]
print(numbers)
print(new_numbers)
