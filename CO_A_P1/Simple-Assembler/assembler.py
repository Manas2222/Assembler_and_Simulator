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
            lst[1] = labels[lst[1]]
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
            lst[1] = labels[lst[1]]
            return JumpIfLessThan(lst)
            
    elif x == 'jgt':
        if len(lst) != 2:
            print("General Syntax Error")
            return -1
        
        if lst[1] not in labels.keys():
            print(f"label {lst[1]} doesn't exits")
            return -1
        else:
            lst[1] = labels[lst[1]]
            return JumpIfGreaterThan(lst)
            
    elif x == 'je':
        if len(lst) != 2:
            print("General Syntax Error")
            return -1
        
        if lst[1] not in labels:
            print(f"label {lst[1]} doesn't exist")
            return -1
        else:
            lst[1] = labels[lst[1]]
            return JumpIfEqual(lst)
    elif x == 'hlt':
        return halt(lst)
    elif x == 'ld':
        # print(f'{lst}')
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



temp_lst_f = sys.stdin.readlines()
instruction_temp = [i.strip() for i in temp_lst_f if i.strip() != '']
# print(instruction_temp)
while True:
    varChecker = True

    if len(instruction_temp) > 128:
        print("Memory overflow: Add less than 128 lines")
        # checker = -1
        break
    
    var_list = []

    # vars
    for i in range (len(instruction_temp)):
        # print(instruction_temp[i].split())
        if (instruction_temp[i].split()[0] != 'var'):
            varChecker = False
        else :
            if varChecker == False:
                print("var commands must be at the beginning")
                varChecker = -1
                break
            else:
                var_list.append(instruction_temp[i].split()[1])


    for i in range (len(var_list)):
        variables[var_list[i]] = (7-len(bin(len(instruction_temp) + i - len(var_list))[2:]))*'0' + (bin(len(instruction_temp) + i - len(var_list))[2:])
    
    for i in range (len(var_list)):
        instruction_temp.pop(0)
    # print(instruction_temp)
    # labels
    lines_to_visit = []
    for i in range (len(instruction_temp)):
        if ':' in instruction_temp[i]:
            idx = instruction_temp[i].find(':')
            # print(idx)
            if instruction_temp[i][:idx] != instruction_temp[i][:idx].strip():
                errorsFound.append("No space allowed between label name and colon")
                errorsFound.append(f"There is error in line numbered at {i+1}")
            if idx == len(instruction_temp[i])-1:
                labels[instruction_temp[i][:idx]] = (7-len(bin(i)[2:]))*'0' + bin(i)[2:]
            else:
                labels[instruction_temp[i][:idx]] = (7-len(bin(i)[2:]))*'0' + bin(i)[2:]
                lines_to_visit.append(i)

    if (len(errorsFound) != 0):
        break
    
    # assemble code
    line = []
    checker = 0
    lastInstruction = 0
    for i in range (len(instruction_temp)):
        lastInstruction += 1

        line = instruction_temp[i].strip().split()
        # print(lines_to_visit)
        if i in lines_to_visit:
            temp_lst = []
            idx = instruction_temp[i].find(':')
            tmp = instruction_temp[i][idx+1:]
            temp_lst = tmp.strip().split()
            if temp_lst != []:
                line = temp_lst
        

        if line[0] == 'st' or line[0] == 'ld':
            if len(line) != 3:
               errorsFound.append(f"There is error in line numbered at {i+len(var_list)+1}")
               print("General syntax error")
               checker = -1
               break
            if line[2] not in variables.keys():
                # print(line)
                # machineCode.append(load(line))
                errorsFound.append(f"There is error in line numbered at {i+len(var_list)+1}")
                print(f"{line[2]}: Variable does not exist")
                checker = -1
                break
            else:
                line[2] = variables[line[2]]
                if (line[0] == 'ld'):
                    # print(load(line))
                    machineCode.append(load(line))
                    continue
                else:
                    # print(store(line))
                    machineCode.append(store(line))
                    continue
            errorsFound.append(f"There is error in line numbered at {i+1}")
            checker = -1
            break
        # print(line)
        if line[0] == 'hlt' and haltInstruction:
            errorsFound.append("Error : Multiple halt statements")
            checker = -1
            break
        if line[0] == 'hlt' and haltInstruction == False:
            haltInstruction = True
        # print(i+1,line)
        data = functionMapper(line)

        if data == "Label":
            continue
        if data == -1:
            # print(1)
            errorsFound.append(f"There is error in line numbered at {i+len(var_list)+1}")
            checker = -1
            break

        # instructionCounter += 1
        # print(data)
        machineCode.append(data)
        if data == '1101000000000000':
            # instructionCounter += 1
            break

    # print(labels)
    if checker == -1:
        break    
    if haltInstruction == True:
        break 

    break



if (len(errorsFound ) == 0):
    if haltInstruction == False:
        errorsFound.append("No halt instruction in the code")
    
    if haltInstruction == True and lastInstruction < len(instruction_temp):
        errorsFound.append("hlt not the last instruction")

if len(machineCode) > 256:
    errorsFound.append("More then 256 lines not allowed")


if (len(errorsFound) != 0):
    for i in errorsFound:
        print(i)
if len(errorsFound) == 0:
    for code in machineCode:
        print(f'{code}')


