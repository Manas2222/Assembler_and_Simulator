# import csv
from Helper import *


def Addition(Lst):
    if (len(Lst) != 4):
        return -1

    if (registers(Lst[1]) == -1 or registers(Lst[2]) == -1 or registers(Lst[3]) == -1):
        return -1

    op_code = opcode(Lst[0])
    if (op_code == -1):
        return -1

    val = op_code + '00' + \
        registers(Lst[1]) + registers(Lst[2]) + registers(Lst[3])

    return val


def Subtraction(Lst):
    if (len(Lst) != 4):
        return -1

    if (registers(Lst[1]) == -1 or registers(Lst[2]) == -1 or registers(Lst[3]) == -1):
        return -1

    op_code = opcode(Lst[0])
    if (op_code == -1):
        return -1
    val = op_code + '00' + \
        registers(Lst[1]) + registers(Lst[2]) + registers(Lst[3])
    return val


def Multiply(Lst):
    if (len(Lst) != 4):
        return -1

    if (registers(Lst[1]) == -1 or registers(Lst[2]) == -1 or registers(Lst[3]) == -1):
        return -1

    op_code = opcode(Lst[0])
    if (op_code == -1):
        return -1
    val = op_code + '00' + \
        registers(Lst[1]) + registers(Lst[2]) + registers(Lst[3])
    return val


def Divide(Lst):
    if (len(Lst) != 3):
        return -1

    if (registers(Lst[1]) == -1 or registers(Lst[2]) == -1 or registers(Lst[3]) == -1):
        return -1

    op_code = opcode(Lst[0])
    if (op_code == -1):
        return -1
    val = op_code + '00000' + registers(Lst[1]) + registers(Lst[2])
    return val


def MoveImmediate(Lst):
    if (len(Lst) != 3):
        return -1

    if (registers(Lst[1]) == -1 or registers(Lst[2]) == -1 or registers(Lst[3]) == -1):
        return -1

    op_code = opcode(Lst[0])
    if (op_code == -1):
        return -1
    if len(str(Lst[2])) != 7:
        return -1
    val = op_code + '0' + registers(Lst[1]) + str(Lst[2])
    return val


def MoveRegister(Lst):
    if (len(Lst) != 3):
        return -1

    if (registers(Lst[1]) == -1 or registers(Lst[2]) == -1 or registers(Lst[3]) == -1):
        return -1

    op_code = opcode(Lst[0])
    if (op_code == -1):
        return -1
    val = op_code + '00000' + registers(Lst[1]) + registers(Lst[2])
    return val


