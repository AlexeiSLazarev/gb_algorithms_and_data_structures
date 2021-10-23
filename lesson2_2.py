'''
Посчитать четные и нечетные цифры введенного натурального числа. 
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 
2 нечетные (3 и 5).
'''

def even_odd(arr):
    if arr == []: return 
    else:
        num = arr.pop()
        even_.append(num) if (num % 2) == 0 else  odd_.append(num)
        even_odd(arr)

input_to_int_list = lambda str_: [int(x) for x in str_]
even_, odd_ = [],[]

even_odd(input_to_int_list(input("Введите целое число: ")))
print(f"Четных цифр - {len(even_)}: ", *even_)
print(f"Нечетных - {len(odd_)}: ", *odd_)


