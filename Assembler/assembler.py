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


