class House:
    def __init__(self, numberOfFloors):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        House.numberOfFloors = floors
        print(House.numberOfFloors)

h1 = House(0)
h1.setNewNumberOfFloors(9)