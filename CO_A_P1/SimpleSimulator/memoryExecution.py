from sys import stdin
from registerExecution import *


class Memory:
'''Functions for working with memory and memory related instructions.'''
    memoryArray = []
    instructionNumber = 0
    
    
    def __init__(self):
        for i in range (128):
            self.memoryArray.append('0000000000000000')
        return


    def initialize(self):
        counter = 0
        for line in stdin:
            self.memoryArray[counter] = str(line)
            counter += 1
        self.instructionNumber = counter
        return


    def resetMemory(self):
        self.memoryArray = []
        self.instructionNumber = 0
        return

    
    def fetchData(self,prgramCounter):
        # instNum = convert7bitStringToInt(prgramCounter)
        instruction = self.memoryArray[prgramCounter]
        return instruction
     

    def loadFromAddress(self,reg1,mem_addr):
        idx = int(mem_addr,2)
        RF.setRegister(reg1,int(self.memoryArray[idx],2))
        return
    

    def storeAtAddress(self,reg1,mem_addr):
        val = RF.getRegister(reg1)
        bin_val = convertIntTo16BitBin(val)
        idx = convert7bitStringToInt(mem_addr)
        self.memoryArray[idx] =  bin_val
        return
    
    
    def dump(self):
        for i in range (len(self.memoryArray)):
            print(self.memoryArray[i])
        return

    # def



MEM = Memory()
