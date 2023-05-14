from Helper import *


def Addition(Lst):
    if (len(Lst) != 4):
        print("General Syntax Error")
        return -1
    
    if (Lst[1] == 'FLAGS' or Lst[2] == 'FLAGS' or Lst[3] == 'FLAGS'):
        print("Illegal use of flags register")
        return -1

    if (registers(Lst[1]) == -1 or registers(Lst[2]) == -1 or registers(Lst[3]) == -1):
        return -1

    op_code = opcode(Lst[0])
    if (op_code == -1):
        return -1

    val = op_code + '00' + registers(Lst[1]) + registers(Lst[2]) + registers(Lst[3])

    return val


def Subtraction(Lst):
    if (len(Lst) != 4):
        print("General Syntax Error")
        return -1
    
    if (Lst[1] == 'FLAGS' or Lst[2] == 'FLAGS' or Lst[3] == 'FLAGS'):
        print("Illegal use of flags register")
        return -1

    if (registers(Lst[1]) == -1 or registers(Lst[2]) == -1 or registers(Lst[3]) == -1):
        return -1

    op_code = opcode(Lst[0])
    if (op_code == -1):
        return -1
    val = op_code + '00' + registers(Lst[1]) + registers(Lst[2]) + registers(Lst[3])
    return val


def Multiply(Lst):
    if (len(Lst) != 4):
        print("General Syntax Error")
        return -1
    
    if (Lst[1] == 'FLAGS' or Lst[2] == 'FLAGS' or Lst[3] == 'FLAGS'):
        print("Illegal use of flags register")
        return -1

    if (registers(Lst[1]) == -1 or registers(Lst[2]) == -1 or registers(Lst[3]) == -1):
        return -1

    op_code = opcode(Lst[0])
    if (op_code == -1):
        return -1
    val = op_code + '00' + registers(Lst[1]) + registers(Lst[2]) + registers(Lst[3])
    return val


def Divide(Lst):
    if (len(Lst) != 3):
        print("General Syntax Error")
        return -1
    
    if (Lst[1] == 'FLAGS' or Lst[2] == 'FLAGS'):
        print("Illegal use of flags register")
        return -1

    if (registers(Lst[1]) == -1 or registers(Lst[2]) == -1):
        return -1

    op_code = opcode(Lst[0])
    if (op_code == -1):
        return -1
    val = op_code + '00000' + registers(Lst[1]) + registers(Lst[2])
    return val


def MoveImmediate(lst):
    if (len(lst) != 3):
        print("General Syntax Error")
        return -1

    if (registers(lst[1]) == -1):
        return -1
    
    if lst[1] == 'FLAGS':
        print("Illegal use of flags register")
        return -1

    op_code = opcode(lst[0])
    if (op_code == -1):
        return -1
    if '.' in lst[2][1:]:
        print("immediate should be whole number")
        return -1
    if not(int(lst[2][1:]) >= 0 and int(lst[2][1:]) <= 127):
        # print("Faulty immediate value")
        print("Illegal immediate value")
        return -1

    imm = bin(int(lst[2][1:]))[2:]
    
    imm_val = (7-len(str(imm)))*'0' + imm
    val = op_code + '0' + registers(lst[1]) + imm_val
    return val
    # pass

def MoveRegister(lst):
    if (len(lst) != 3):
        print("General Syntax Error")
        return -1

    if (registers(lst[1]) == -1 or registers(lst[2]) == -1):
        return -1
    
    if lst[1] == 'FLAGS':
        print("Move command doesn't support flags as first register")
        return -1

    op_code = opcode("mov_reg")
    if (op_code == -1):
        return -1
    val = op_code + '00000' + registers(lst[1]) + registers(lst[2])
    return val
    

# lst1_2 = ['mov','R3','$0']
# answer = MoveImmediate(lst1_2)
# print(answer)