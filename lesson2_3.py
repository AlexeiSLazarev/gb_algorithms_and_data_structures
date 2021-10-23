'''
Сформировать из введенного числа обратное по порядку входящих в него цифр 
и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.
'''
x_reverse = []
def reverse_(x):
    if x==[]: return
    else:
        x_reverse.append(x.pop())
        reverse_(x)

split_by_char = lambda str: [x for x in str]

x = split_by_char(input("Введите число: "))
reverse_(x)
print("В обратной последовательности: ", *x_reverse, sep = '')
