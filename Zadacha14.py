#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

#10 -> 1 2 4 8

import math 

N = int(input())

d = 0

while math.pow(2, d) < N:
    d += 1
    print(int(math.pow(2, d-1)))


