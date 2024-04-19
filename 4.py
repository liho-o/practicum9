"""
Конкурс рыболовов собрал команды из разных стран.
Задание одного из шуточных конкурса заключается в том, чтобы каждая команда сплела сеть из N веревок.

Задание считается выполненным, если получается сеть, в которой каждая веревка связана ровно с тремя другими.

Напишите программу, определяющую сколько команд смогут справиться с этим заданием.

Программа получает на вход некоторое количество чисел N - число веревок, выданное команде.
Каждое значение вводится в отдельной строке. Количество команд не известно.
Окончанием ввода данных является значение 0.

Программа должна вывести одно число - количество команд, способных выполнить задание.
"""


def inp_num():
    comm_list = []
    while True:
        num = int(input())
        if num == 0:
            return comm_list
        else:
            comm_list.append(num)


def check_list(list_comm):
    i = 0
    for comm in list_comm:
        if comm % 4 == 0:
            i += 1
    return i


list_comm = inp_num()
print(check_list(list_comm))
