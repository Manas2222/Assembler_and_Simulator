from Helper import *


def halt(lst):
    if len(lst) != 1:
        return -1
    
    opcod = opcode(lst[0])

    if (opcod == -1):
        return -1
    
    return opcod + "00000000000"



def UnconditionaJump(lst):
    # l1=['0']*16
    # oc=opcode(str1)
    # if oc==-1:
    #     errorlist.append("JMP OP -1")
    #     return -1
    
    # for i in range(len(oc)):
    #     l1[i]=oc[i]
    # if var.isalnum():
    #     #sees the memory of the variable
    #     pass

    
    # elif var.isdigit():
    #     if len(var)!=7:
    #             errorlist.append('JMP MEM -1')
    #             return -1
    #     for i in range(9,16):
    #         l1[i]=var[i-9]
    # return ''.join(l1)
    if len(lst) != 2:
        return -1
    
    opcod = opcode(lst[0])
    if opcod == -1:
        return -1
    
    if len(lst[1]) != 7:
        return -1

    return opcod + '0000' + lst[1]

def JumpIfLessThan(lst):
    # l1=['0']*16
    # oc=opcode(str1)
    # if oc==-1:
    #     errorlist.append("JLT OP -1")
    #     return -1
    
    # for i in range(len(oc)):
    #     l1[i]=oc[i]
    # if var.isalnum():
    #     #sees the memory of the variable
    #     pass


    # elif var.isdigit():
    #     if len(var)!=7:
    #         errorlist.append('JLT MEM -1')
    #         return -1
    #     for i in range(9,16):
    #         l1[i]=var[i-9]
    # return ''.join(l1)
    if len(lst) != 2:
        return -1
    
    opcod = opcode(lst[0])
    if opcod == -1:
        return -1
    
    if len(lst[1]) != 7:
        return -1

    return opcod + '0000' + lst[1]


    
def JumpIfGreaterThan(lst):
    # l1=['0']*16
    # oc=opcode(str1)
    # if oc==-1:
    #     errorlist.append("JGT OP -1")
    #     return -1
    
    # for i in range(len(oc)):
    #     l1[i]=oc[i]
    # if var.isalnum():
    #     #sees the memory of the variable
    #     pass


    # elif var.isdigit():
    #     if len(var)!=7:
    #         errorlist.append('JGT MEM -1')
    #         return -1
    #     for i in range(9,16):
    #         l1[i]=var[i-9]
    # return ''.join(l1)
    if len(lst) != 2:
        return -1
    
    opcod = opcode(lst[0])
    if opcod == -1:
        return -1
    
    if len(lst[1]) != 7:
        return -1

    return opcod + '0000' + lst[1]
    

def JumpIfEqual(lst):

    # l1=['0']*16
    # oc=opcode(str1)
    # if oc==-1:
    #     errorlist.append("JE OP -1")
    #     return -1
    
    # for i in range(len(oc)):
    #     l1[i]=oc[i]
    # if var.isalnum():
    #     #sees the memory of the variable
    #     pass


    # elif var.isdigit():
    #     if len(var)!=7:
    #         errorlist.append('JE MEM -1')
    #         return -1
    #     for i in range(9,16):
    #         l1[i]=var[i-9]

    # return ''.join(l1)
    if len(lst)  != 2:
        return -1
    
    opcod = opcode(lst[0])
    if opcod == -1:
        return -1
    
    if len(lst[1]) != 7:
        return -1

    return opcod + '0000' + lst[1]

