# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    def fib(N):
        a, b = 1, 1
        for i in range(1, N):
            a, b = b, a + b
        return b
    return [fib(x) for x in range(n, m + 1)]


print(fibonacci(int(input("Введите номер начальной позиции ряда ")),
                int(input("Введите номер конечной позиции ряда "))))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def my_filter(a, b):
    ls = []
    for i in b:
        if i <= a:
            ls.append(i)
    return ls


print(my_filter(5, [2, 29, 235, 24, 6, 3, 5, 3, 1, 0]))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

