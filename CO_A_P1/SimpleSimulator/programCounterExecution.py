


class progCounter:

    progCounter = 0


    def __init__(self):
        self.progCounter = 0


    def getPC(self):
        return self.progCounter()
    

    def update(self,val):
        self.progCounter = val



PC = progCounter()
