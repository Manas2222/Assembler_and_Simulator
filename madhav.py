from Helper import *


def halt(lst):
    if len(lst) != 1:
        print("General Syntax Error")
        return -1
    
    opcod = opcode(lst[0])

    if (opcod == -1):
        return -1
    
    return opcod + "00000000000"



def UnconditionaJump(lst):
    if len(lst) != 2:
        print("General Syntax Error")
        return -1
    
    opcod = opcode(lst[0])
    if opcod == -1:
        return -1
    
    if len(lst[1]) != 7:
        return -1

    return opcod + '0000' + lst[1]

def JumpIfLessThan(lst):
    if len(lst) != 2:
        print("General Syntax Error")
        return -1
    
    opcod = opcode(lst[0])
    if opcod == -1:
        return -1
    
    if len(lst[1]) != 7:
        return -1

    return opcod + '0000' + lst[1]


    
def JumpIfGreaterThan(lst):
    if len(lst) != 2:
        print("General Syntax Error")
        return -1
    
    opcod = opcode(lst[0])
    if opcod == -1:
        return -1
    
    if len(lst[1]) != 7:
        return -1

    return opcod + '0000' + lst[1]
    

def JumpIfEqual(lst):
    if len(lst)  != 2:
        print("General Syntax Error")
        return -1
    
    opcod = opcode(lst[0])
    if opcod == -1:
        return -1
    
    if len(lst[1]) != 7:
        return -1

    return opcod + '0000' + lst[1]

