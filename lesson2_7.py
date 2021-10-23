'''
Напишите программу, доказывающую или проверяющую, 
что для множества натуральных чисел выполняется равенство: 
1+2+...+n = n(n+1)/2, где n - любое натуральное число.
'''

def l_side(n): return 0 if n==0 else n + l_side(n - 1)
def r_side(n): return n*(n+1)/2
def compare_lr(l,r): return "Да" if l == r else "Нет"

n = int(input("Введите n:"))
print(f"Правда ли, что для n = {n}, 1+2+...+n = n(n+1)/2:", compare_lr(l_side(n),r_side(n)))
print('Левая часть выражения = ', l_side(n))
print('Правая часть выражения =', r_side(n))

