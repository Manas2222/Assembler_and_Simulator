
def convertIntTo7BitBin(data):
    ans = bin(data)[2:].zfill(7)
    return ans


class ProgCounter:

    progCounter = 0


    def __init__(self):
        self.progCounter = 0


    def getPC(self):
        return self.progCounter
    

    def update(self,val):
        self.progCounter = val

    def dump(self):
        print(convertIntTo7BitBin(self.progCounter), end=' ')


PC = ProgCounter()
