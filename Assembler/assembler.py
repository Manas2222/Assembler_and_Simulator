from instructions import *

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
    
with open("Input.txt") as f:
    lst = f.readlines()

instruction = [i.strip().split(' ') for i in lst]

# print(lst)
# print(instruction)

for i in instruction:
    if (i[0][-1] == ':'):
        # labels[i[0][:-1]] =
        pass 
    else:
        print(functionMapper(i))

