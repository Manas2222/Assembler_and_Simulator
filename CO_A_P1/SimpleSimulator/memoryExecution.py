from sys import stdin
from registerExecution import *


class Memory:

    memoryArray = []
    instructionNumber = 0
    
    
    def __init__(self):
        for i in range (256):
            self.memoryArray.append('0000000000000000')


    def initialize(self):
        counter = 0
        for line in stdin:
            self.memoryArray[counter] = str(line)
            counter += 1
        self.instructionNumber = counter

    
    def fetchData(self,prgramCounter):
        instNum = convert7bitStringToBin(prgramCounter)
        instruction = self.memoryArray[instNum]
        return instruction
    



    