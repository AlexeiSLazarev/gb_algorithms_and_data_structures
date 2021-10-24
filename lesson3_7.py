'''
В одномерном массиве целых чисел определить два наименьших элемента. 
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
'''

import random 
arr = [random.randint(0, 20) for i in range(5)] 

print("Оригинальный массив: ", *arr)

min_val1 = arr.pop([id for id,val in enumerate(arr) if val==min(arr)][0])
min_val2 = arr.pop([id for id,val in enumerate(arr) if val==min(arr)][0])

print(f"Первое минимальное значение: {min_val1}.")
print(f"Первое минимальное значение: {min_val2}.")