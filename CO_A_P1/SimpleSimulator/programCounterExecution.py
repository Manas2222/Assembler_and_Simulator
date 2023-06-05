
def convertIntTo7BitBin(data):
    ans = bin(data)[2:].zfill(7)
    return ans


class ProgCounter:
'''Taking progcounter as -1 for defualt'''
    progCounter = -1


    def __init__(self):
        self.progCounter = 0
        return


    def getPC(self):
        return self.progCounter
    

    def resetCounter(self):
        self.progCounter = -1
        return

'''Updating the counter to its value'''
    def update(self,val):
        self.progCounter = val
        return


    def dump(self):
        print(convertIntTo7BitBin(self.progCounter), end=' ')
        return



PC = ProgCounter()
