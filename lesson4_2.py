'''
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. 
Результаты анализа сохранить в виде комментариев в файле с кодом.

Сложность алгоритма нахождения i-го по счёту простого числа с использованием «Решета Эратосфена» - O(NloglogN)
Анализ времени в файле lesson4_2.png
'''

# Функция вычисления i-ого по счету простого числа без использования «Решета Эратосфена».
def get_n_prime1(n):
    arr_prime = []
    num = 1
    while len(arr_prime)<n:
        num +=1
        cntr = 0
        for cur_num in range(1, num+1):
            if num%cur_num==0:
                cntr+=1
        if cntr == 2:
            arr_prime.append(num)
    return arr_prime

def is_new_prime(num, arr_prime):
    flag = True
    for pn in arr_prime:
        if num%pn==0: flag = False
    return flag

# Функция вычисления i-ого по счету простого числа с использованием элементов «Решета Эратосфена». 
# Некий ее "динамический" вариант.
def get_n_prime2(n):
    arr_prime = []
    num = 1
    while len(arr_prime)<n:
        num +=1
        if is_new_prime(num, arr_prime): arr_prime.append(num)

    return arr_prime



import timeit

target_prime = []
proc_time1 = []
proc_time2 = []
for i in  range(12):
    k = 50*i
    target_prime.append(int(k))
    t = timeit.Timer(f"get_n_prime1({k})", "from __main__ import get_n_prime1")
    proc_time1.append(float(t.timeit(1)))

    t = timeit.Timer(f"get_n_prime2({k})", "from __main__ import get_n_prime2")
    proc_time2.append(float(t.timeit(1)))



import matplotlib.pyplot as plt

plt.plot(target_prime, proc_time1, label="без \'решета\'")
plt.plot(target_prime, proc_time2, label="с \'решетом\'")
plt.legend(loc="upper left")
plt.xlabel("Номер простого числа.")
plt.ylabel("Время поиска i-го числа, сек.")
plt.title("Графики зависимостей времени поиска i-го простого числа от n.")
plt.show()