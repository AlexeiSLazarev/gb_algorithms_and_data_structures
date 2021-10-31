'''
Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

В качестве примера возьмем алгоритм из задачи 7 урока №2:

************************************************
Напишите программу, доказывающую или проверяющую, 
что для множества натуральных чисел выполняется равенство: 
1+2+...+n = n(n+1)/2, где n - любое натуральное число.
************************************************

Cожность алгоритма вычисления левой части - O(n), правой - O(1)

Анализ скорости выполнения для n = 1000000:

  Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.115    0.115 <string>:1(<module>)
        1    0.115    0.115    0.115    0.115 lesson4_1.py:9(l_side)
        1    0.000    0.000    0.115    0.115 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 lesson4_1.py:15(r_side)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''


def l_side(n): 
    sum = 0 
    for i in range(1,n+1):
        sum += i
    return sum

def r_side(n): return n*(n+1)/2
def compare_lr(l,r): return "Да" if l == r else "Нет"

n = int(input("Введите n:"))

l_s = l_side(n)
r_s = r_side(n)

print(f"Правда ли, что для n = {n}, 1+2+...+n = n(n+1)/2:", compare_lr(l_s,r_s))
print('Левая часть выражения = ', l_s)
print('Правая часть выражения =', r_s)

import cProfile
cProfile.run('l_side(n)')
cProfile.run('r_side(n)')