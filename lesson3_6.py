'''
В одномерном массиве найти сумму элементов, 
находящихся между минимальным и максимальным элементами. 
Сами минимальный и максимальный элементы в сумму не включать.

'''

import random 
arr = [random.randint(0, 20) for i in range(5)] 

print("Оригинальный массив: ", *arr)

min_val = min(arr)
max_val = max(arr)
id_min = [id for id,val in enumerate(arr) if val==min_val][0]
id_max = [id for id,val in enumerate(arr) if val==max_val][0]

print(f"id min = {id_min}, id max = {id_max},")
print(f"Сумма значений между мин. и макс. = {sum(arr[id_min+1:id_max])}")