'''
Написать программу сложения и умножения двух шестнадцатеричных чисел. 
При этом каждое число представляется как массив, элементы которого это цифры числа. 
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] 
соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - 
[‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''

a = input("Введите a: ")
b = input("Введите b: ")

# Cложение
from collections import deque 
queue1 = deque([ch.upper() for ch in a])
queue2 = deque([ch.upper() for ch in b])

add = '0'
res_arr = []
while queue1 or queue2:
    if queue1: a1 = queue1.pop()
    else:      a1 = '0'
    
    if queue2: b1 = queue2.pop()
    else:      b1 = '0'

    sum_ = str(hex(int(a1, 16) + int(b1, 16) + int(add, 16)))[2:]
    sum_chrs = deque([ch.upper() for ch in sum_])
    if len(sum_chrs) > 1:
        res_arr.append(sum_chrs[1])
        add = sum_chrs[0]
    else:
        res_arr.append(sum_chrs[0])
        add = '0'
if add != '0': res_arr.append(add)
res_arr.reverse()
print("Сумма = ", *res_arr)


# Умножение
mult_ = [ch.upper() for ch in str(hex(int(a, 16) * int(b, 16)))[2:]]
print("Произведение = ", *mult_)