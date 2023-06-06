from registerExecution import *
from programCounterExecution import *
from memoryExecution import *

class EngineExecution:

    # instruction = ''

    def execute(self,instruction):
        '''Normal convention in below code followed is 
        first taking the registers which are to be used 
        then performing the operation expected and
        checking for any possible overflow or any other condition
        then incrementing the program counter and ressetting the flag if not used.'''

        haltEncountered = False
        programCounter = 0
        opcode_ = instruction[0:5]
        
        if opcode_ == '00000':

            tempReg1 = instruction[7:10]
            tempReg2 = instruction[10:13]
            tempReg3 = instruction[13:16]

            answer =  RF.getRegister(tempReg2) + RF.getRegister(tempReg3)

            RF.setRegister(tempReg1,answer)
            if overflowChecker(answer) == True:
                RF.setOverflow()
            else:
                RF.defaultFlag()

            # PC.update(PC.getPC() + 1)
            haltEncountered = False
            programCounter = PC.getPC() + 1

        elif opcode_ == '00001':
            tempReg1 = instruction[7:10]
            tempReg2 = instruction[10:13]
            tempReg3 = instruction[13:16]

            answer =  RF.getRegister(tempReg2) - RF.getRegister(tempReg3)
            RF.setRegister(tempReg1,answer)
            if answer < 0:
                RF.setOverflow()
                answer = 0
            else:
                RF.defaultFlag()
            
            # PC.update(PC.getPC() + 1)
            haltEncountered = False
            programCounter = PC.getPC() + 1

        elif opcode_ == '00010':
            tempReg1 = instruction[6:9]
            immVal = instruction[9:]

            RF.setRegister(tempReg1,int(immVal,2))
            # PC.update(PC.getPC() + 1)
            haltEncountered = False
            programCounter = PC.getPC() + 1
            RF.defaultFlag()
        
        elif opcode_ == '00011':
            tempReg1 = instruction[10:13]
            tempReg2 = instruction[13:16]
            reg2Val = RF.getRegister(tempReg2)
            RF.setRegister(tempReg1,reg2Val)
            # PC.update(PC.getPC() + 1)
            haltEncountered = False
            programCounter = PC.getPC() + 1
            RF.defaultFlag()
        
        elif opcode_ == '00100':
            tempReg1 = instruction[6:9]
            mem_addr = instruction[9:]
            MEM.loadFromAddress(tempReg1,mem_addr)
            RF.defaultFlag()
            # PC.update(PC.getPC() + 1)
            haltEncountered = False
            programCounter = PC.getPC() + 1
        
        elif opcode_ == '00101':
            tempReg1 = instruction[6:9]
            mem_addr = instruction[9:]
            MEM.sloadFromAddress(tempReg1,mem_addr)
            RF.defaultFlag()
            # PC.update(PC.getPC() + 1)
            haltEncountered = False
            programCounter = PC.getPC() + 1

        elif opcode_ == '00110':
            tempReg1 = instruction[7:10]
            tempReg2 = instruction[10:13]
            tempReg3 = instruction[13:16]
            ans = RF.getRegister(tempReg2) * RF.getRegister(tempReg3)
            RF.setRegister(tempReg1,answer)
            if overflowChecker(answer) == True:
                RF.setOverflow()
            else:
                RF.defaultFlag()

            # PC.update(PC.getPC() + 1)
            haltEncountered = False
            programCounter = PC.getPC() + 1

        elif opcode_ == '00111':
            tempReg1 = instruction[10:13]
            tempReg2 = instruction[13:16]
            val1 = RF.getRegister(tempReg1)
            val2 = RF.getRegister(tempReg2)
            RF.setRegister('000',val1//val2)
            RF.setRegister('001',(val1%val2))
            # PC.update(PC.getPC() + 1)
            haltEncountered = False
            programCounter = PC.getPC() + 1
            

        elif opcode_ == '01000':
            tempReg1 = instruction[6:9]
            imm = instruction[9:]
            value = RF.getRegister(tempReg1)
            imm_val = int(imm,2)
            answer = value >> imm_val
            # answer_ = convertIntTo16BitBin(answer)
            RF.setRegister(tempReg1,answer)
            RF.defaultFlag()
            haltEncountered = False
            programCounter = PC.getPC() + 1

        elif opcode_ == '01001':
            tempReg1 = instruction[6:9]
            imm = instruction[9:]
            value = RF.getRegister(tempReg1)
            imm_val = int(imm,2)
            answer = value << imm_val
            # answer_ = convertIntTo16BitBin(answer)
            RF.setRegister(tempReg1,answer)
            # if overflowChecker(answer) == True:
            #     RF.setOverflow()
            # else:
            #     RF.defaultFlag()
            RF.defaultFlag()
            haltEncountered = False
            programCounter = PC.getPC() + 1
        
        elif opcode_ == '01010':
            tempReg1 = instruction[7:10]
            tempReg2 = instruction[10:13]
            tempReg3 = instruction[13:16]
            val1 = RF.getRegister(tempReg2)
            val2 = RF.getRegister(tempReg3)
            answer = val1 ^ val2
            RF.setRegister(tempReg1,answer)
            RF.defaultFlag()
            haltEncountered = False
            programCounter = PC.getPC() + 1
        
        elif opcode_ == '01011':
            tempReg1 = instruction[7:10]
            tempReg2 = instruction[10:13]
            tempReg3 = instruction[13:16]
            val1 = RF.getRegister(tempReg2)
            val2 = RF.getRegister(tempReg3)
            answer = val1 | val2
            RF.setRegister(tempReg1,answer)
            RF.defaultFlag()
            haltEncountered = False
            programCounter = PC.getPC() + 1

        elif opcode_ == '01100':
            tempReg1 = instruction[7:10]
            tempReg2 = instruction[10:13]
            tempReg3 = instruction[13:16]
            val1 = RF.getRegister(tempReg2)
            val2 = RF.getRegister(tempReg3)
            answer = val1 & val2
            RF.setRegister(tempReg1,answer)
            RF.defaultFlag()
            haltEncountered = False
            programCounter = PC.getPC() + 1

        elif opcode_== '01101':
            tempReg1 = instruction[10:13]
            tempReg2 = instruction[13:16]
            val1 = RF.getRegister(tempReg2)
            temp = convertIntTo16BitBin(val1)
            inverted_num = ''
            for i in range(len(temp)):
                if temp[i] == '0':
                    inverted_num += '1'
                else:
                    inverted_num += '0'
            RF.setRegister(tempReg1,int(inverted_num,2))
            RF.defaultFlag()
            haltEncountered = False
            programCounter = PC.getPC() + 1
        
        elif opcode_ == '01110':
            tempReg1 = instruction[10:13]
            tempReg2 = instruction[13:16]
            val1 = RF.getRegister(tempReg1)
            val2 = RF.getRegister(tempReg2)
            if val1 > val2:
                RF.setFlagGreater()
            elif val1 < val2:
                RF.setFlagLess()
            else:
                RF.setFlagEqual()
            haltEncountered = False
            programCounter = PC.getPC() + 1

        elif opcode_ == '01111':
            mem_addr = instruction[9:]
            haltEncountered = False
            programCounter = int(mem_addr,2)
            RF.defaultFlag()

        elif opcode_ == '11100':
            mem_addr = instruction[9:]
            if RF.getRegister('111') == '0000000000000100':
                programCounter = int(mem_addr,2)
            else:
                programCounter = PC.getPC() + 1
            haltEncountered = False
            RF.defaultFlag()
        
        elif opcode_ == '11101':
            mem_addr = instruction[9:]
            if RF.getRegister('111') == '0000000000000010':
                programCounter = int(mem_addr,2)
            else:
                programCounter = PC.getPC() + 1
            haltEncountered = False
            RF.defaultFlag()

        elif opcode_ == '11111':
            mem_addr = instruction[9:]
            if RF.getRegister('111') == '0000000000000001':
                programCounter = int(mem_addr,2)
            else:
                programCounter = PC.getPC() + 1
            haltEncountered = False
            RF.defaultFlag()

        elif opcode_ == '11010':
            haltEncountered = True
            programCounter = PC.getPC() + 1
            RF.defaultFlag()
            PC.resetCounter()
            RF.resetRegisters()
            MEM.resetMemory()
        return haltEncountered,programCounter
    

EE = EngineExecution()
