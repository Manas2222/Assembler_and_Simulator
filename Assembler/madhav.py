from Helper import *


def halt(lst):
    f = open("stdout.txt",'a')
    if len(lst) != 1:
        f.write("General Syntax Error\n")
        return -1
    
    opcod = opcode(lst[0])

    if (opcod == -1):
        return -1
    
    return opcod + "00000000000"



def UnconditionaJump(lst):
    f = open("stdout.txt",'a')
    if len(lst) != 2:
        f.write("General Syntax Error\n")
        return -1
    
    opcod = opcode(lst[0])
    if opcod == -1:
        return -1
    
    if len(lst[1]) != 7:
        return -1

    return opcod + '0000' + lst[1]

def JumpIfLessThan(lst):
    f = open("stdout.txt",'a')
    if len(lst) != 2:
        f.write("General Syntax Error\n")
        return -1
    
    opcod = opcode(lst[0])
    if opcod == -1:
        return -1
    
    if len(lst[1]) != 7:
        return -1

    return opcod + '0000' + lst[1]


    
def JumpIfGreaterThan(lst):
    f = open("stdout.txt",'a')
    if len(lst) != 2:
        f.write("General Syntax Error\n")
        return -1
    
    opcod = opcode(lst[0])
    if opcod == -1:
        return -1
    
    if len(lst[1]) != 7:
        return -1

    return opcod + '0000' + lst[1]
    

def JumpIfEqual(lst):
    f = open("stdout.txt",'a')
    if len(lst)  != 2:
        f.write("General Syntax Error\n")
        return -1
    
    opcod = opcode(lst[0])
    if opcod == -1:
        return -1
    
    if len(lst[1]) != 7:
        return -1

    return opcod + '0000' + lst[1]

