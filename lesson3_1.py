'''
В диапазоне натуральных чисел от 2 до 99 определить, 
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
'''

res ={}
for i in range(2,9):
    cntr = 0
    for j in range(2,99):
        if j%i == 0:
            cntr+=1
    res[i]=cntr
print(res)