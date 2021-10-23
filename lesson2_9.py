'''
Среди натуральных чисел, которые были введены, 
найти наибольшее по сумме цифр. 
Вывести на экран это число и сумму его цифр.
'''
def sum_digits(str_):
    str_to_int = lambda str: [x for x in str_]
    return sum(list(map(int, str_to_int(str))))

numbers = input("Введите числа через \",\": ").split(',')
num_dig_sum = list(map(sum_digits,numbers))
max_dig_sum = max(num_dig_sum)
print(f"Максимальная сумма цифр = {max_dig_sum} в числе {numbers[num_dig_sum.index(max_dig_sum)]}.")