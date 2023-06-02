from registerExecution import *
from programCounterExecution import *


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

            if overflowChecker(answer) == True:
                RF.setOverflow()
            else:
                RF.defaultFlag()

            RF.setRegister(tempReg1,answer)
            PC.incrementPC()
            haltEncountered = False
            programCounter = PC.getPC

        if opcode_ == '00001':
            tempReg1 = instruction[7:10]
            tempReg2 = instruction[10:13]
            tempReg3 = instruction[13:16]

            answer =  RF.getRegister(tempReg2) - RF.getRegister(tempReg3)
            if answer < 0:
                RF.setOverflow()
                answer = 0
            else:
                RF.defaultFlag()
            
            RF.setRegister(tempReg1,answer)
            PC.incrementPC()
            haltEncountered = False
            programCounter = PC.getPC()

        if opcode_ == '00010':
            tempReg1 = instruction[6:9]
            immVal = instruction[9:]

            RF.setRegister(tempReg1,int(immVal,2))
            PC.incrementPC()
            haltEncountered = False
            programCounter = PC.getPC
            RF.defaultFlag()
        
        if opcode_ == '00011':
            tempReg1 = instruction[10:13]
            tempReg2 = instruction[13:16]
            reg2Val = RF.getRegister(tempReg2)
            RF.setRegister(tempReg1,reg2Val)
            PC.incrementPC()
            haltEncountered = False
            programCounter = PC.getPC
            RF.defaultFlag()
        



        