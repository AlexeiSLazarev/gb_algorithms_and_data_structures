'''
Задача:
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
'''

n = int(input('Введите номер буквы в алфавите: '))
if (n > 0) and (n <= 33):
    n = ord('a') + n - 1
    print(chr(n))
    print('Это буква', chr(n))
else:
    print("Номер буквы должен быть между 1 и 33.")