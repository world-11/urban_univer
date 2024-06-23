class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        # new_floor = 1
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(new_floor):
                print(i+1)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('Перекоп', 2)
h4 = House('11', 7)
h1.go_to(5)
h2.go_to(10)
h3.go_to(2)
h4.go_to(12)