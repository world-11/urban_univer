class House:
    def __init__(self, numberOfFloors):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)

h1 = House(0)
h1.setNewNumberOfFloors(9)