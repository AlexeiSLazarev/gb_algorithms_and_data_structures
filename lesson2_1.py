'''
Написать программу, которая будет складывать, вычитать, умножать или делить два числа. 
Числа и знак операции вводятся пользователем. 
После выполнения вычисления программа не должна завершаться, 
а должна запрашивать новые данные для вычислений. 
Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. 
Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), 
то программа должна сообщать ему об ошибке и снова запрашивать знак операции. 
Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 
в качестве делителя.
'''
while True:
    x = list(map(int, input("Введите два числа через \',\': ").split(',')))
    op = input("Введите один из операторов +,-,*,/ или 0 если хотите выйти: ")
    if op == '0': break
    else:
        res = eval(f"{x[0]} {op} {x[1]}")
        print(f"Результат: {x[0]} {op} {x[1]} = {res}.")