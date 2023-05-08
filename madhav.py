
def opcode(var):
    opcodes = {
        'add' : '00000',
        'sub' : '00001',
        'mov' : '00010',
        'mov_reg' : '00011',
        'ld' : '00100',
        'st' : '00101',
        'mul' : '00110',
        'div' : '00111',
        'rs' : '01000',
        'ls' : '01001',
        'xor' : '01010',
        'or' : '01011',
        'and' : '01100',
        'not' : '01101',
        'cmp' : '01110',
        'jmp' : '01111',
        'jlt' : '11100',
        'jgt' : '11101',
        'je' : '11111',
        'hlt' : '11010'

    }
    if var in opcodes.keys():
        return opcodes[var]
    return -1

def registers(var):
    register = {
        'R1' : '000',
        'R2' : '001',
        'R3' : '010',
        'R4' : '011',
        'R5' : '100',
        'R6' : '110',
        'R7' : '111'
    }

    if var in register.keys():
        return registers[var]
    return -1


def halt(str1):
    l1=['0']*16
    val=(opcode(str1))

    if val==-1:
        return -1
    else:
        
        for i in range(len(val)):
            l1[i]=val[i]
    return ''.join(l1)
    #put a quit() command in the main after catching this



def UnconditionaJump(str1,var):
    l1=['0']*16
    oc=opcode(str1)
    if oc==-1:
        print("Invalid command")
        return -1
    
    for i in range(len(oc)):
        l1[i]=oc[i]
    if var.isalnum():
        #sees the memory of the variable
        pass

    
    elif var.isdigit():
        if len(var)!=7:
                print('lenght of memory address not proper')
                return -1
        for i in range(9,16):
            l1[i]=var[i-9]
    return ''.join(l1)

def JumpIfLessThan(str1,var):
    l1=['0']*16
    oc=opcode(str1)
    if oc==-1:
        print("Invalid command")
        return -1
    if flag[13]=='1':
        for i in range(len(oc)):
            l1[i]=oc[i]
        if var.isalnum():
            #sees the memory of the variable
            pass

    
        elif var.isdigit():
            if len(var)!=7:
                print('lenght of memory address not proper')
                return -1
            for i in range(9,16):
                l1[i]=var[i-9]
        return ''.join(l1)
    return 2

    
def JumpIfGreaterThan(str1,var):
    l1=['0']*16
    oc=opcode(str1)
    if oc==-1:
        print("Invalid command")
        return -1
    if flag[14]=='1':
        for i in range(len(oc)):
            l1[i]=oc[i]
        if var.isalnum():
            #sees the memory of the variable
            pass

    
        elif var.isdigit():
            if len(var)!=7:
                print('lenght of memory address not proper')
                return -1
            for i in range(9,16):
                l1[i]=var[i-9]
        return ''.join(l1)
    return 2

def JumpIfEqual(str1,var):

    l1=['0']*16
    oc=opcode(str1)
    if oc==-1:
        print("Invalid command")
        return -1
    if flag[15]=='1':
        for i in range(len(oc)):
            l1[i]=oc[i]
        if var.isalnum():
            #sees the memory of the variable
            pass

    
        elif var.isdigit():
            if len(var)!=7:
                print('lenght of memory address not proper')
                return -1
            for i in range(9,16):
                l1[i]=var[i-9]
    
        return ''.join(l1)
    return 2
    

