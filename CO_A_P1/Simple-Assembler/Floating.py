from Helper import *


def add_floating(lst):
    if len(lst) != 4:
        return -1
    
    if (lst[1] == 'FLAGS' or lst[2] == 'FLAGS' or lst[3] == 'FLAGS'):
        print("Illegal use of flags register")
        return -1
    
    if (registers(lst[1]) == -1 or registers(lst[2]) == -1 or registers(lst[3]) == -1):
        return -1

    op_code = opcode(lst[0])
    if (op_code == -1):
        return -1
    
    val = op_code + '00' + registers(lst[1]) + registers(lst[2]) + registers(lst[3])

    return val

def sub_floating(lst):
    if len(lst) != 4:
        return -1
    
    if (lst[1] == 'FLAGS' or lst[2] == 'FLAGS' or lst[3] == 'FLAGS'):
        print("Illegal use of flags register")
        return -1
    
    if (registers(lst[1]) == -1 or registers(lst[2]) == -1 or registers(lst[3]) == -1):
        return -1

    op_code = opcode(lst[0])
    if (op_code == -1):
        return -1
    
    val = op_code + '00' + registers(lst[1]) + registers(lst[2]) + registers(lst[3])

    return val

def mov_floating(lst):
    if len(lst) != 4:
        return -1
    
    if (lst[1] == 'FLAGS' or lst[2] == 'FLAGS' or lst[3] == 'FLAGS'):
        print("Illegal use of flags register")
        return -1
    
    if (registers(lst[1]) == -1 or registers(lst[2]) == -1 or registers(lst[3]) == -1):
        return -1

    op_code = opcode(lst[0])
    if (op_code == -1):
        return -1
    
    val = op_code + '00' + registers(lst[1]) + registers(lst[2]) + registers(lst[3])

    return val