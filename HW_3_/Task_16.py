'''Задача 16: Требуется вычислить, 
сколько раз встречается некоторое число X в массиве A. 
Пользователь в первой строке вводит натуральное число N 
– количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию). 
Последняя строка содержит число X.

*Пример:*

5
    7 -2 3 5 1
    3
    -> 1'''
n = int(input("Введите натуральное число N для задания количества элементов в массиве: "))
# print(n)
import random
lst = [random.randint(-10, 10) for i in range(n)]
print(lst)
x = int(input("Введите число , которое нужно найти в массиве: "))

sum = 0
for i in range(n):
    if lst[i] == x:
        sum += 1
print(f"{sum} раз(а) встречается  число {x} в заданном массиве")