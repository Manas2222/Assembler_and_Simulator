from manas import *
from madhav import *
from alok import *
from mayank import *
import sys


errorsFound = []
labels = {}
variables = {}
machineCode = []
haltInstruction = False
instructionCounter = 0

def load(lst):
    if len(lst) != 3:
        print("General Syntax Error")
        return -1
    
    if lst[1] == 'R7':
        print("Illegal use of flag register")

    if registers(lst[1]) == -1:
        return -1
    
    opcod = opcode(lst[0])
    if opcod == -1:
        return -1
    
    val = opcod + '0' + registers(lst[1]) + lst[2]
    return val

def store(lst):
    if len(lst) != 3:
        print("General Syntax Error")
        return -1
    
    if lst[1] == 'R7':
        print("Illegal use of flag register")
        return -1
    
    if registers(lst[1]) == -1:
        return -1
    
    opcod = opcode(lst[0])
    if opcod == -1:
        return -1
    
    val = opcod + '0' + registers(lst[1]) + lst[2]
    return val

    


def functionMapper(lst):
    x = lst[0]
    if x == 'xor':
        return exclusive_or(lst)
    elif x == 'or':
        return Or(lst)
    elif x == 'and':
        return And(lst)
    elif x == 'not':
        return invert(lst)
    elif x == 'cmp':
        return compare(lst)
    elif x == 'add':
        return Addition(lst)
    elif x == 'sub':
        return Subtraction(lst)
    elif x == 'mov':
        if len(lst) != 3:
            return -1
        if lst[2][0] == '$':
            return MoveImmediate(lst)
        else:
            return MoveRegister(lst)
    elif x == 'mul':
        return Multiply(lst)
    elif x == 'div':
        return Divide(lst)
    elif x == 'rs':
        return right_shift(lst)
    elif x == 'ls':
        return left_shift(lst)
    elif x == 'jmp':
        if len(lst) != 2:
            print("General Syntax Error")
            return -1
        
        if lst[1] not in labels.keys():
            print(f"label {lst[1]} doesn't exist")
            return -1
        else:
            lst[1] = labels[lst[1]][0]
            return UnconditionaJump(lst)

        # return UnconditionaJump(lst)
    elif x == 'jlt':
        if len(lst) != 2:
            print("General Syntax Error")
            return -1
        
        if lst[1] not in labels.keys():
            print(f"label {lst[1]} doesn't exist")
            return -1
        else:
            lst[1] = labels[lst[1]][0]
            return JumpIfLessThan(lst)
            
    elif x == 'jgt':
        if len(lst) != 2:
            print("General Syntax Error")
            return -1
        
        if lst[1] not in labels.keys():
            print(f"label {lst[1]} doesn't exits")
            return -1
        else:
            lst[1] = labels[lst[1]][0]
            return JumpIfGreaterThan(lst)
            
    elif x == 'je':
        if len(lst) != 2:
            print("General Syntax Error")
            return -1
        
        if lst[1] not in labels:
            print(f"label {lst[1]} doesn't exist")
            return -1
        else:
            lst[1] = labels[lst[1]][0]
            return JumpIfEqual(lst)
    elif x == 'hlt':
        return halt(lst)
    elif x == 'ld':
        print(lst)
        if len(lst) != 3:
            print("General Syntax Error")
            return -1
        if lst[2] in variables.keys():
            lst[2] = variables[lst[2]]
            return load(lst)
        
        print("Wrong address")
        return -1
    elif x == 'st':
        if len(lst) != 3:
            print("General Syntax Error")
            return -1
        if lst[2] in variables.keys():
            lst[2] = variables[lst[2]]
            return store(lst)
        print("Wrong address")
        return -1
    elif x[-1] == ':':
        return "Label"
    print("Typo in instruction name")
    return -1



instruction_temp = []
for line in sys.stdin:
    instruction_temp.append(line.strip())


label_lines_to_visit = []
for i in range (len(instruction_temp)):
    if ':' in instruction_temp[i]:
        idx = instruction_temp[i].find(':')
        # print(idx)
        if instruction_temp[i][:idx] != instruction_temp[i][:idx].strip():
            errorsFound.append("No space allowed between label name and colon")
        if idx == len(instruction_temp[i])-1:
            labels[instruction_temp[i][:-1]] = [(7 - len(bin(127-len(labels.keys()))[2:]))*'0' + bin(127-len(labels.keys()))[2:] , i+1]
        else:
            label_lines_to_visit.append(i)
            labels[instruction_temp[i][:idx]] = [(7 - len(bin(127-len(labels.keys()))[2:]))*'0' + bin(127-len(labels.keys()))[2:] , i+1]
    
instruction_temp = [i.strip().split() for i in instruction_temp]
# print(instruction_temp)
varChecker = False
lastInstuction = 0
line = []
if len(errorsFound) == 0:
    for i in range (len(instruction_temp)):
        lastInstuction+=1

        if instruction_temp[i] == '':
            continue

        line = instruction_temp[i]

        if i in label_lines_to_visit:
            lst_tmp = []
            for j in range (1,len(instruction_temp[i])):
                lst_tmp.append(instruction_temp[i][j])
            line = lst_tmp

        if line[0] == 'var':
            if varChecker == True:
                errorsFound.append("All variables must be defined in the beginning")
                break
            variables[line[1]] = (7 - len(bin(0 + len(variables.keys()))[2:]))*'0' + bin(0 + len(variables.keys()))[2:]
        else:
            varChecker = True
            if line[0] == 'st' or line[0] == 'ld':
                if len(line) != 3:
                    errorsFound.append(f"There is error in line numbered at {i+1}")
                    print("General syntax error")
                    break
                if line[2] not in variables.keys():
                    print(line)
                    # machineCode.append(load(line))
                    print(f"memory address in '{line[0]}' must be an existant variable")
                else:
                    line[2] = variables[line[2]]
                    if (line[0] == 'ld'):
                        machineCode.append(load(line))
                        continue
                    else:
                        machineCode.append(store(line))
                        continue
                errorsFound.append(f"There is error in line numbered at {i+1}")
                break
            if line[0] == 'hlt' and haltInstruction:
                errorsFound.append("Error : Multiple halt statements")
                break
            if line[0] == 'hlt' and haltInstruction == False:
                haltInstruction = True
            data = functionMapper(line)
            
            if data == "Label":
                continue
            if data == -1:
                errorsFound.append(f"There is error in line numbered at {i+1}")
                break
            instructionCounter += 1
            machineCode.append(data)
            if data == '1101000000000000':
                instructionCounter += 1
                break

if len(errorsFound) == 0:
    if haltInstruction == False:
        errorsFound.append("No halt instruction in the code")
    # print("last_inst = ",lastInstuction)
    if haltInstruction == True and lastInstuction < len(instruction_temp):
        errorsFound.append("hlt not the last instruction")
if len(errorsFound) == 0:
    for code in machineCode:
        print(code)

for errors in errorsFound:
    print(errors)


