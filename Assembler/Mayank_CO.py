from Helper import *


# lst = [ls, r1, $imm]
def right_shift(lst):
    if(len(lst) != 3):
        return -1
    if(registers(lst[1]) == -1 or opcode(lst[0]) == -1):
        return -1
    if not(int(lst[2][1:])>=0 and int(lst[2][1:])<=127):
        return -1
    
    opcoddd = opcode(lst[0])
    reg1 = registers(lst[1])
    imm_val = bin(int(lst[2][1:]))
    
    
    
    
    opcode_ans = opcoddd + '0' + (7-len(imm_val[2:]))*'0' + reg1 + imm_val
    
    return opcode_ans

def left_shift(lst):
    if(len(lst) != 3):
        return -1
    if(registers(lst[1]) == -1 or opcode(lst[0]) == -1):
        return -1
    #Later add case for error found 
    if not(int(lst[2][1:])>=0 and int(lst[2][1:])<=127):
        return -1
    opcoddd = opcode(lst[0])
    reg1 = registers(lst[1])
    imm_val = bin(int(lst[2][1:]))

    
    
    opcode_ans = opcoddd + '0' + reg1 + (7-len(imm_val[2:]))*'0' + imm_val[2:]
    
    return opcode_ans
    

# lst1_4 = ['ls','R3','$31']
# answer = left_shift(lst1_4)
# print(answer)