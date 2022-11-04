"""Создайте функцию three_args(), которая принимает 1, 2 или 3 строго ключевых параметра.
В результате ее работы на печать в консоль выводятся значения переданных переменных, но только если они не равны None.
Получим, например, следующее сообщение: «Переданы аргументы: var1 = 2, var3 = 10»."""

def three_args(var1, var2, var3):
    return f'Переданы аргументы: var1 = {var1}, var2 = {var2}, var3 = {var3}».'
first_parametr = int(input())
second_parametr = int(input())
third_parametr = int(input())
print(three_args(first_parametr, second_parametr, third_parametr))
