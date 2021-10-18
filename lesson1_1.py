'''
Задача:
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

'''

print("Введите трехзначное число:")
input_string = input()

if len(input_string) ==3 and input_string.isdecimal():
    sum_ = 0
    multi_ = 1
    for char in input_string:
        sum_ += int(char)
        multi_ *= int(char)
    print("Сумма цифр = {}".format(sum_))
    print("Произведение цифр = {}".format(multi_))
else:
    print("Строка должна состоять из трех цифр.")