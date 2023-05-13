from instructions import *
from madhav import *
from Alok_CO_project import *
from Mayank_CO import *



errorsFound = []
labels = {}
variables = {}
machineCode = []
haltInstruction = []

def load(lst):
    if len(lst) != 3:
        return -1
    
    if registers(lst[1]) == -1:
        return -1
    
    opcod = opcode(lst[0])
    if opcod == -1:
        return -1
    
    val = opcod + '0' + registers(lst[1]) + lst[2]
    return val

def store(lst):
    if len(lst) != 3:
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
        return UnconditionaJump(lst)
    elif x == 'jlt':
        return JumpIfLessThan(lst)
    elif x == 'jgt':
        return JumpIfGreaterThan(lst)
    elif x == 'je':
        return JumpIfEqual(lst)
    elif x == 'hlt':
        return halt(lst)
    elif x == 'ld':
        print(lst)
        if len(lst) != 3:
            return -1
        if lst[2] in variables.keys():
            lst[2] = variables[lst[2]]
            return load(lst)
        if len(lst[2]) == 7 and checkIfBinary(lst[2]):
            return load(lst)
        
        print("Wrong address")
        return -1
    elif x == 'st':
        if len(lst) != 3:
            return -1
        if lst[2] in variables.keys():
            lst[2] = variables[lst[2]]
            return store(lst)
        if len(lst[2]) == 7 and checkIfBinary(lst[2]):
            return store(lst)
        print("Wrong address")
        return -1

    print("Typo in instruction name")
    return -1




with open("Input.txt") as f:
    lst = f.readlines()

instruction = [i.strip().split() for i in lst if i.strip().split() != [] ]

print(lst)
print(instruction)

varChecker = False
for i in range (len(instruction)):
    # if (instruction[i] == ''):
    #     pass
    if (instruction[i][0][-1] == ':'):
        varChecker = True
        if instruction[i][0][:-1] == instruction[i][0][:-1].split():
            errorsFound.append("No space after label allowed")
            break
        if instruction[i][0][:-1] in labels.keys():
            errorsFound.append("label already exists")
            break
        labels[instruction[i][0][:-1]] = (7 - len(bin(127-len(labels.keys()))[2:]))*'0' + bin(127-len(labels.keys()))[2:]

    elif instruction[i][0] == 'var':
        if varChecker == True:
            errorsFound.append("All variables must be defined in the beginning")
            break
        variables[instruction[i][1]] = (7 - len(bin(0 + len(variables.keys()))[2:]))*'0' + bin(0 + len(variables.keys()))[2:]
        # print(f"added var {lst[0]} with val = {(7 - len(bin(0 + len(variables.keys()))[2:]))*'0' + bin(0 + len(variables.keys()))[2:]}")

    else:
        varChecker = True
        if instruction[i][0] == 'st' or instruction[i][0] == 'ld':
            if len(instruction[i]) != 3:
                errorsFound.append(f"There is error in line numbered at {i+1} (after removing empty lines)")
                print("General syntax error")
                break
            if checkIfBinary(instruction[i][1]) == True:
                machineCode.append(load(instruction[i]))
            else:
                if instruction[i][2] not in variables.keys():
                    errorsFound.append(f"There is error in line numbered at {i+1} (after removing empty lines)")
                    print("No such variable exists")
                    break
                else:
                    instruction[i][2] = variables[instruction[i][2]]
                    machineCode.append(load(instruction[i]))
                    continue
            errorsFound.append(f"There is error in line numbered at {i+1} (after removing empty lines)")
            break

        if functionMapper(instruction[i]) == -1:
            errorsFound.append(f"There is error in line numbered at {i+1} (after removing empty lines)")
            break
        # if functionMapper(instruction[i]) == -1:
        #     errorsFound.append(f"There is error in line numbered at {i+1} (after removing empty lines)")
        #     break
        machineCode.append(functionMapper(instruction[i]))

for errors in errorsFound:
    print(errors)
# print(variables)
for code in machineCode:
    print(code)

