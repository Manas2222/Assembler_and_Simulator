from memoryExecution import *
from programCounterExecution import *
from engineExecution import *
from registerExecution import *




MEM.initialize()
progCounter = 0
counteredHalt = False

while (not counteredHalt):
    instruction = MEM.fetchData(progCounter)
    counteredHalt, newPC = EE.execute(instruction)
    PC.dump()
    RF.dump()
    PC.update(newPC)

MEM.dump()
