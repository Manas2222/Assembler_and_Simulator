flag=[0]*16
errorlist=[]

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
    errorlist.append("GLB OP -1")
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
    errorlist.append("GLB REG -1")
    return -1


def halt(str1):
    l1=['0']*16
    val=(opcode(str1))

    if val==-1:
        errorlist.append("HALT OP -1")
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
        errorlist.append("JMP OP -1")
        return -1
    
    for i in range(len(oc)):
        l1[i]=oc[i]
    if var.isalnum():
        #sees the memory of the variable
        pass

    
    elif var.isdigit():
        if len(var)!=7:
                errorlist.append('JMP MEM -1')
                return -1
        for i in range(9,16):
            l1[i]=var[i-9]
    return ''.join(l1)

def JumpIfLessThan(str1,var):
    l1=['0']*16
    oc=opcode(str1)
    if oc==-1:
        errorlist.append("JLT OP -1")
        return -1
    
    for i in range(len(oc)):
        l1[i]=oc[i]
    if var.isalnum():
        #sees the memory of the variable
        pass


    elif var.isdigit():
        if len(var)!=7:
            errorlist.append('JLT MEM -1')
            return -1
        for i in range(9,16):
            l1[i]=var[i-9]
    return ''.join(l1)


    
def JumpIfGreaterThan(str1,var):
    l1=['0']*16
    oc=opcode(str1)
    if oc==-1:
        errorlist.append("JGT OP -1")
        return -1
    
    for i in range(len(oc)):
        l1[i]=oc[i]
    if var.isalnum():
        #sees the memory of the variable
        pass


    elif var.isdigit():
        if len(var)!=7:
            errorlist.append('JGT MEM -1')
            return -1
        for i in range(9,16):
            l1[i]=var[i-9]
    return ''.join(l1)
    

def JumpIfEqual(str1,var):

    l1=['0']*16
    oc=opcode(str1)
    if oc==-1:
        errorlist.append("JE OP -1")
        return -1
    
    for i in range(len(oc)):
        l1[i]=oc[i]
    if var.isalnum():
        #sees the memory of the variable
        pass


    elif var.isdigit():
        if len(var)!=7:
            errorlist.append('JE MEM -1')
            return -1
        for i in range(9,16):
            l1[i]=var[i-9]

    return ''.join(l1)



    
    


    



'''ALOK'S PORTION'''




def Addition(Lst):
    if (len(Lst) !=4 ):
        errorlist.append('ADD CMD -1')
        return -1
    

    if (registers(Lst[1]) == -1 or registers(Lst[2]) == -1 or registers(Lst[3]) == -1):
        errorlist.append("ADD REG -1")
        return -1
    
    op_code = opcode(Lst[0])
    if (op_code == -1): 
        errorlist.append('ADD OP -1')
        return -1
    
    val = op_code + '00' + registers(Lst[1]) + registers(Lst[2]) + registers(Lst[3])

    return val

def Subtraction(Lst):
    if (len(Lst) !=4 ):
        errorlist.append('SUB CMD -1')
        return -1
    

    if (registers(Lst[1]) == -1 or registers(Lst[2]) == -1 or registers(Lst[3]) == -1):
        errorlist.append("SUB REG -1")
        return -1
    
    op_code = opcode(Lst[0])
    if (op_code == -1): 
        errorlist.append('SUB OP -1')
        return -1
    val = op_code + '00' + registers(Lst[1]) + registers(Lst[2]) + registers(Lst[3])
    return val

def Multiply(Lst):
    if (len(Lst) !=4 ):
        errorlist.append('MUL CMD -1')
        return -1
    

    if (registers(Lst[1]) == -1 or registers(Lst[2]) == -1 or registers(Lst[3]) == -1):
        errorlist.append("MUL REG -1")
        return -1
    
    op_code = opcode(Lst[0])
    if (op_code == -1): 
        errorlist.append('MUL OP -1')
        return -1
    val = op_code + '00' + registers(Lst[1]) + registers(Lst[2]) + registers(Lst[3])
    return val

def Divide(Lst):
    if (len(Lst) !=3):
        errorlist.append('DIV CMD -1')
        return -1
    

    if (registers(Lst[1]) == -1 or registers(Lst[2]) == -1 or registers(Lst[3]) == -1):
        errorlist.append("DIV REG -1")
        return -1
    
    op_code = opcode(Lst[0])
    if (op_code == -1): 
        errorlist.append('DIV OP -1')
        return -1
    val = op_code + '00000' + registers(Lst[1]) + registers(Lst[2])
    return val

def MoveImmediate(Lst):
    if (len(Lst) !=3):
        errorlist.append('MOVIMM CMD -1')
        return -1
    

    if (registers(Lst[1]) == -1 or registers(Lst[2]) == -1 or registers(Lst[3]) == -1):
        errorlist.append("MOVIMM REG -1")
        return -1
    
    op_code = opcode(Lst[0])
    if (op_code == -1): 
        errorlist.append('MOVIMM OP -1')
        return -1
    if len(str(Lst[2]))!=7:
        errorlist.append('MOVIMM IMM -1')
    val = op_code + '0' + registers(Lst[1]) + str(Lst[2])
    return val
def MoveRegister(Lst):
    if (len(Lst) !=3):
        errorlist.append('MOVRIG CMD -1')
        return -1
    

    if (registers(Lst[1]) == -1 or registers(Lst[2]) == -1 or registers(Lst[3]) == -1):
        errorlist.append("MOVRIG REG -1")
        return -1
    
    op_code = opcode(Lst[0])
    if (op_code == -1): 
        errorlist.append('MOVRIG OP -1')
        return -1
    val = op_code + '00000' + registers(Lst[1]) + registers(Lst[2])
    return val

    



    





