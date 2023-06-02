




memory.initialize()
progCounter = 0
counteredHalt = False

while (not counteredHalt):
    instruction = memory.fetchData(progCounter)
    counteredHalt, newPC = EE.execute(instruction)
    PC.dump()
    RF.dump()
    PC.update(newPC)

MEM.dump()
