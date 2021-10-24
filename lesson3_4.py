'''
Определить, какое число в массиве встречается чаще всего.
'''

def find_same_elements(arr, x):
    cntr = 0
    for xi in arr: 
        if xi == x:
            cntr+=1 
    return cntr


arr = [8, 3, 15, 6, 4, 2, 2, 3, 3]
myset = set(arr)
res = {}
for x in myset:
    res[x] = find_same_elements(arr, x)

print(f"Элемент {max(res, key=res.get)} встречается чаще всего - {res[max(res, key=res.get)]} раз(а).")