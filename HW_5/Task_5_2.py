'''Задача 28: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.

*Пример:*

2 2
    4 '''


def sum(b):

    if b == a:
        return b + a
    if b > a:
        return(sum(b - 1) + 1)
    elif b < a: 
        return(sum(b+1)-1)
a = int(input("введите целое неотрицательное число А: "))
b = int(input("введите целое неотрицательное число B: ")) 
print(sum(b))
