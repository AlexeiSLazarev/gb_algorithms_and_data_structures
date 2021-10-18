"""
Задача:
Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число;
случайное вещественное число;
случайный символ.

"""

from random import randint, uniform

data_type = input("Введите тип данных i(nteger)|f(loat)|c(haracters): ")
start = input("Введите начальное значение: ")
end = input("Введите конечное значение: ")

if data_type == 'i':
    r = randint(int(start), int(end))
elif data_type == 'f':
    r = uniform(float(start), float(end))
elif data_type == 'c':
    r = chr(randint(ord(start), ord(end)))
else:
    r = f"Неизвестный тип данных '{data_type}'"

print(f"Случайное значение в диапазоне от {start} до {end} = {r}")
