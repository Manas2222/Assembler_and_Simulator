from memoryExecution import *
from programCounterExecution import *
from engineExecution import *
from registerExecution import *


'''Initialing and running of each machine code until halt isn't encountered'''

MEM.initialize()
progCounter = 0
counteredHalt = False
# print(1)
while (not counteredHalt):
    instruction = MEM.fetchData(PC.getPC())
    counteredHalt, newPC = EE.execute(instruction)
    # print(counteredHalt,newPC)
    # print(instruction)
    PC.dump()
    RF.dump()
    PC.update(newPC)

MEM.dump()
RF.defaultFlag()
PC.resetCounter()
RF.resetRegisters()
MEM.resetMemory()