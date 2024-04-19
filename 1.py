"""
Имеется цепочка, состоящая из N колец.
Толщина каждого кольца d мм, внутренний радиус каждого кольца - R мм.
Напишите программу, которая определяет длину цепочки L.
На рисунке представлена цепочка из N=3 колец.
В одной строке, через пробел должны вводится с клавиатуры целые числа N, d и R.
Программа должна выводить одно число L - длину цепочки в мм.
Программа допускает реализацию в виде линейного алгоритмома и может быть решена без условного оператора.
"""
import math
n, d, r = map(int, input().split())


def l_returned(n, d, r):
    n1 = n % 2
    l = n * (2 * (r + d)) - (2 * d) - n1 * (2 * d)
    return l


print(l_returned(n, d, r))
