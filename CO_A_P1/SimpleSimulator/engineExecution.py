from registerExecution import *
from programCounterExecution import *
from memoryExecution import *

class EngineExecution:

    # instruction = ''

    def execute(self,instruction):

        haltEncountered, programCounter = False,0
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
            programCounter = PC.getPC + 1

        if opcode_ == '00001':
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

        if opcode_ == '00010':
            tempReg1 = instruction[6:9]
            immVal = instruction[9:]

            RF.setRegister(tempReg1,int(immVal,2))
            # PC.update(PC.getPC() + 1)
            haltEncountered = False
            programCounter = PC.getPC + 1
            RF.defaultFlag()
        
        if opcode_ == '00011':
            tempReg1 = instruction[10:13]
            tempReg2 = instruction[13:16]
            reg2Val = RF.getRegister(tempReg2)
            RF.setRegister(tempReg1,reg2Val)
            # PC.update(PC.getPC() + 1)
            haltEncountered = False
            programCounter = PC.getPC + 1
            RF.defaultFlag()
        
        if opcode_ == '00100':
            tempReg1 = instruction[6:9]
            mem_addr = instruction[9:]
            MEM.loadFromAddress(tempReg1,mem_addr)
            RF.defaultFlag()
            # PC.update(PC.getPC() + 1)
            haltEncountered = False
            programCounter = PC.getPC() + 1
        
        if opcode_ == '00101':
            tempReg1 = instruction[6:9]
            mem_addr = instruction[9:]
            MEM.storeAtAddress(tempReg1,mem_addr)
            RF.defaultFlag()
            # PC.update(PC.getPC() + 1)
            haltEncountered = False
            programCounter = PC.getPC() + 1

        if opcode_ == '00110':
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

        if opcode_ == '00111':
            tempReg1 = instruction[10:13]
            tempReg2 = instruction[13:16]
            val1 = RF.getRegister(tempReg1)
            val2 = RF.getRegister(tempReg2)
            RF.setRegister('000',val1//val2)
            RF.setRegister('001',(val1%val2))
            # PC.update(PC.getPC() + 1)
            haltEncountered = False
            programCounter = PC.getPC() + 1
            

        if opcode_ == '01000':
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

        if opcode_ == '01001':
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
        
        if opcode_ == '01010':
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
        
        # if opcode_ == ''
