
'''
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. 
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Также укажите в комментариях версию Python и разрядность вашей ОС.
Разрядность ОС: 64-bit
Python 3.8
'''

'''
Из задания lesson3_2
Во втором массиве сохранить индексы четных элементов первого массива. 
'''
import random
import sys

@profile
def my_func():
    arr = [random.randint(0,100) for i in range(10000)]
    # print("В массиве: ", *arr)
    ids = [i for i,j in enumerate(arr) if j%2==0]
    # print("Индексы четных чисел:", *ids)
    print("Размер начального массива: ", sys.getsizeof(arr))
    print("Размер массива индекса четных чисел: ", sys.getsizeof(ids))
    return ids

if __name__ == '__main__':
    my_func()


'''
python3 -m memory_profiler lesson5_1.py
Размер начального массива:  87616
Размер массива индекса четных чисел:  43032
Filename: lesson5_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    19   18.652 MiB   18.652 MiB           1   @profile
    20                                         def my_func():
    21   18.652 MiB    0.000 MiB       10003       arr = [random.randint(0,100) for i in range(10000)]
    22                                             # print("В массиве: ", *arr)
    23   18.871 MiB    0.219 MiB       10003       ids = [i for i,j in enumerate(arr) if j%2==0]
    24                                             # print("Индексы четных чисел:", *ids)
    25   18.871 MiB    0.000 MiB           1       print("Размер начального массива: ", sys.getsizeof(arr))
    26   18.871 MiB    0.000 MiB           1       print("Размер массива индекса четных чисел: ", sys.getsizeof(ids))
    27   18.871 MiB    0.000 MiB           1       return ids
'''