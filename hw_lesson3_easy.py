# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    temp_number = number * (10 ** ndigits)
    point_position = str(temp_number)
    pos_of_dec = point_position.find('.')
    if point_position[pos_of_dec + 1] in ['5', '6', '7', '8', '9']:
        temp_number += 1
    temp_number = temp_number // 1
    temp_number = temp_number / (10 ** ndigits)
    return temp_number


print(my_round(float(input("Введите число ")),
               int(input("Введите количество знаков после запятой для округления "))))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    digits = [int(i) for i in str(ticket_number)]
    if len(digits) != 6:
        return "У вас обычный билет"
    first_half = sum(digits[:3])
    second_half = sum(digits[3:])
    if first_half == second_half:
        return "У вас счастливый билет!"
    else:
        return "У вас обычный билет"


print(lucky_ticket(input("Введите шестизначный номер билета ")))



