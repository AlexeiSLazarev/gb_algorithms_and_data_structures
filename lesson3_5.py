'''
В массиве найти максимальный отрицательный элемент. 
Вывести на экран его значение и позицию в массиве.
'''

import random 
arr = [random.randint(-10, 10) for i in range(5)] 

print("Оригинальный массив: ", *arr)

min_val = min(arr)
if min_val < 0:
    id_min = [id for id,val in enumerate(arr) if val==min_val][0]
    print(f"Максимальный отрицательный элемент: {min_val}. \n Позиция в массиве {id_min}")
else:
    print("В массиве нет отрицательных значений.")