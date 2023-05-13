from instructions import *
from madhav import *
from Alok_CO_project import *
from Mayank_CO import *



errorsFound = []
labels = {}
variables = {}
machineCode = []
haltInstruction = []




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
        pass
    elif x == 'st':
        pass
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

    else:
        varChecker = True
        if functionMapper(instruction[i]) == -1:
            errorsFound.append("There is error in line numbered at ",i, "(after removing empty lines)")
            break
        print(functionMapper(instruction[i]))



