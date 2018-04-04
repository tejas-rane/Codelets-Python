class Enemy:
    def __init__(self, x=2):
        self.energy = x
    def getEnergy(self):
        print(self.energy)

json = Enemy()
Sandy = Enemy(5)

json.getEnergy()
Sandy.getEnergy()

print(Sandy.energy)