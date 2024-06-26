class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return  self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

h1 = Building(13, 'admin')
h2 = Building(14, 'admin')
h3 = Building(13, 'production')
h4 = Building(13, 'admin')

print(h1 == h4)
print(h1 == h2)
print(h1 == h3)
