'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

import random 
arr = [random.randint(0, 20) for i in range(5)] 

print("Оригинальный массив: ", *arr)

min_val = min(arr)
max_val = max(arr)
id_min = [id for id,val in enumerate(arr) if val==min_val][0]
id_max = [id for id,val in enumerate(arr) if val==max_val][0]

arr[id_min] = max_val
arr[id_max] = min_val

print("Min и max заменены: ", *arr)