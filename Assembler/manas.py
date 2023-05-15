from Helper import *

# lst['add','R1','R2','R3']

def exclusive_or(lst):
    f = open("stdout.txt",'a')
    if (len(lst) != 4):
        f.write("General Syntax Error\n")
        return -1
    # if ((int(lst[1][-1]) > 7 and int(lst[1][-1]) < 0) or (int(lst[2][-1]) > 7 and int(lst[2][-1]) < 0) or (int(lst[3][-1]) > 7 and int(lst[3][-1]) < 0)):
    #     return False
        # We will change the flag register in the main function if any function returns false :)
    if (lst[1] == 'FLAGS' or lst[2] == 'FLAGS' or lst[3] == 'FLAGS'):
        f.write("Illegal use of flags register\n")
        return -1

    if (registers(lst[1]) == -1 or registers(lst[2]) == -1 or registers(lst[3]) == -1):
        errors += 1
        return -1
    op_code = opcode(lst[0])
    if (op_code == -1):
        errorsFound +=1
        return -1
    op_code = op_code + '00' +  registers(lst[1]) + registers(lst[2]) + registers(lst[3])
    return op_code


def Or(lst):
    f = open("stdout.txt",'a')
    if (len(lst) != 4):
        f.write("General Syntax Error\n")
        return -1
    
    if (lst[1] == 'FLAGS' or lst[2] == 'FLAGS' or lst[3] == 'FLAGS'):
        f.write("Illegal use of flags register\n")
        return -1

    if (registers(lst[1]) == -1 or registers(lst[2]) == -1 or registers(lst[3]) == -1):
        return -1
    
    op_code = opcode(lst[0])
    if (op_code == -1):
        return -1
    op_code = op_code + '00' + registers(lst[1]) + registers(lst[2]) + registers(lst[3])
    return op_code


def And(lst):
    f = open("stdout.txt",'a')
    if (len(lst) != 4):
        f.write("General Syntax Error\n")
        return -1
    
    if (lst[1] == 'FLAGS' or lst[2] == 'FLAGS' or lst[3] == 'FLAGS'):
        f.write("Illegal use of flags register\n")
        return -1

    if (registers(lst[1]) == -1 or registers(lst[2]) == -1 or registers(lst[3]) == -1):
        return -1
    
    op_code = opcode(lst[0])
    if (op_code == -1):
        return -1
    op_code = op_code + '00' + registers(lst[1]) + registers(lst[2]) + registers(lst[3])
    return op_code


def invert(lst):
    f = open("stdout.txt",'a')
    if (len(lst) != 3):
        f.write("General Syntax Error\n")
        return -1
    
    if (lst[1] == 'FLAGS' or lst[2] == 'FLAGS'):
        f.write("Illegal use of flags register\n")
        return -1

    if (registers(lst[1]) == -1 or registers(lst[2]) == -1):
        return -1
    
    op_code = opcode(lst[0])
    if (op_code == -1):
        return -1
    op_code = op_code + '00000' + registers(lst[1]) + registers(lst[2])
    return op_code


def compare(lst):
    f = open("stdout.txt",'a')
    if (len(lst) != 3):
        f.write("General Syntax Error\n")
        return -1
    
    if (lst[1] == 'FLAGS' or lst[2] == 'FLAGS'):
        f.write("Illegal use of flags register\n")
        return -1

    if (registers(lst[1]) == -1 or registers(lst[2]) == -1 ):
        return -1
    
    op_code = opcode(lst[0])
    if (op_code == -1):
        return -1
    op_code = op_code + '00000' + registers(lst[1]) + registers(lst[2])
    return op_code



